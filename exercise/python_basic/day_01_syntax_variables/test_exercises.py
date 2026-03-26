"""Pytest checks for Day 01 exercises.

These tests are expected to fail until the learner implements each exercise stub.
"""

from __future__ import annotations

import importlib.util
from pathlib import Path

import pytest


BASE_DIR = Path(__file__).parent


def _load_module(filename: str):
    path = BASE_DIR / filename
    spec = importlib.util.spec_from_file_location(path.stem, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Unable to load module: {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


ex01 = _load_module("ex01_basic.py")
ex02 = _load_module("ex02_intermediate.py")
ex03 = _load_module("ex03_advanced.py")


def test_ex01_format_username_happy_path() -> None:
    assert ex01.format_username("  Alice Doe  ") == "alice_doe"


def test_ex01_format_username_blank() -> None:
    with pytest.raises(ValueError):
        ex01.format_username("   ")


@pytest.mark.parametrize(
    ("raw", "expected"),
    [("0", 0), ("3", 3), ("5", 5)],
)
def test_ex02_parse_retry_count_valid(raw: str, expected: int) -> None:
    assert ex02.parse_retry_count(raw) == expected


@pytest.mark.parametrize("raw", ["-1", "6", "abc"])
def test_ex02_parse_retry_count_invalid(raw: str) -> None:
    with pytest.raises(ValueError):
        ex02.parse_retry_count(raw)


def test_ex03_build_runtime_banner_happy_path() -> None:
    output = ex03.build_runtime_banner("InventoryAPI", "prod", False, 4)
    assert output == "[PROD] app=InventoryAPI debug=False workers=4"


@pytest.mark.parametrize(
    ("app_name", "env", "debug", "workers"),
    [("", "prod", False, 4), ("Billing", "prod", True, 0)],
)
def test_ex03_build_runtime_banner_invalid(
    app_name: str,
    env: str,
    debug: bool,
    workers: int,
) -> None:
    with pytest.raises(ValueError):
        ex03.build_runtime_banner(app_name, env, debug, workers)
