from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from opt_public_server.common.settings import get_settings


app = FastAPI(
    debug=True,
    title=get_settings().app_title,
    description=get_settings().app_description,
    version=get_settings().app_version,
    contact={
        "name": get_settings().author_name,
        "url": get_settings().website,
    },
    license_info={
        "name": get_settings().app_license,
    },
)


@app.get("/")
def index():
    return RedirectResponse("/graphql")
