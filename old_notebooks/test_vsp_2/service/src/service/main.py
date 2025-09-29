from contextlib import asynccontextmanager

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from starlette.staticfiles import StaticFiles
import uvicorn

from service.dependencies import with_settings
from service.kernel import HttpKernel
from service.routes import router

settings = with_settings()


@asynccontextmanager
async def lifespan(app: FastAPI):
    client = HttpKernel(str(settings.pharia_kernel_address))
    yield {"kernel": client}
    await client.shutdown()


app = FastAPI(lifespan=lifespan)

###############################################################################
# WARNING: Do not modify this CORS configuration unless you fully understand    #
# the Pharia Applications Proxy implications.                                   #
#                                                                              #
# This configuration is strictly for local development/preview purposes.        #
# In production deployments, CORS is automatically handled by PhariaAI.     #
# Modifying these settings in production will cause header conflicts.           #
###############################################################################
if settings.enable_cors:
    app.add_middleware(
        CORSMiddleware,  # type: ignore
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["GET", "POST"],
        allow_headers=["*"],
    )

app.include_router(router)


###############################################################################
# WARNING: Do not modify the UI serving configuration below unless you fully    #
# understand the implications.                                                  #
#                                                                              #
# The StaticFiles mount is required to serve the Application UI in          #
# PhariaAssistant.                                                            #
###############################################################################
app.mount("/ui", StaticFiles(directory="ui-artifacts"), name="ui")


def main():
    uvicorn.run("service.main:app", host="0.0.0.0", port=8080)


if __name__ == "__main__":
    main()
