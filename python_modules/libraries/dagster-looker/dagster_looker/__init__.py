from dagster._core.libraries import DagsterLibraryRegistry

from dagster_looker.api.resource import LookerResource as LookerResource
from dagster_looker.lkml.asset_specs import build_looker_asset_specs as build_looker_asset_specs
from dagster_looker.lkml.dagster_looker_translator import (
    DagsterLookerTranslator as DagsterLookerTranslator,
    LookMLStructureType as LookMLStructureType,
)
from dagster_looker.version import __version__ as __version__

DagsterLibraryRegistry.register("dagster-looker", __version__)
