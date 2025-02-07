import typing as T

import logfire
from fastapi import APIRouter, status, Depends, FastAPI, Security
from fastapi import HTTPException
from sqlalchemy import func
from sqlalchemy.orm import Session
from sqlmodel import select

from . import settings
from .schemas import (
    Etablissement,
    EtablissementPublicAvecResultats,
    FsUser,
    QueryParameters,
    get_db,
)
from .auth import supabase_auth


app = FastAPI(
    title="Fireset API",
    summary="A contact server to store your contacts' information",
    description="A contact server to store your contacts' information",
    version="1.0.0",
    root_path=settings.api_path,
)
router = APIRouter()

logfire.instrument_fastapi(app)


@router.get("/etablissement/{uai}", response_model=EtablissementPublicAvecResultats)
async def read_etablissement(
    uai: str,
    user: FsUser = Security(supabase_auth),
    db: Session = Depends(get_db),
) -> EtablissementPublicAvecResultats:
    stmt = select(Etablissement).where(Etablissement.UAI == uai)

    a = list(db.scalars(stmt))
    if len(a) == 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Etablissement '{uai}' not found"
        )
    else:
        etab = a[0]

    return etab


@router.post("/etablissements", response_model=T.List[EtablissementPublicAvecResultats])
async def etablissement_in_zone(
    body: QueryParameters,
    user: FsUser = Security(supabase_auth),
    db: Session = Depends(get_db),
) -> T.List[EtablissementPublicAvecResultats]:
    stmt = select(Etablissement).where(func.ST_Within(Etablissement.position, body.iso.getGeom()))

    if body.nature is not None and body.nature != []:
        stmt = stmt.where(Etablissement.nature.in_(body.nature))

    if body.secteur is not None and body.secteur != []:
        stmt = stmt.where(Etablissement.secteur.in_(body.secteur))

    a = db.scalars(stmt)

    return list(a)


@router.get("/user", response_model=FsUser)
async def get_user(
    user: FsUser = Security(supabase_auth),
) -> FsUser:
    return user


app.include_router(router)
