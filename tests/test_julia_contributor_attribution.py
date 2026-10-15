from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read(relative):
    return (ROOT / relative).read_text(encoding="utf-8")


def test_project_and_julia_contributor_credit():
    assert "Soheil Salmani" in read("README.md")
    assert "Mahdieh Moghiseh" in read("README.md")
    assert "Mahdieh Moghiseh" in read("CONTRIBUTORS.md")
    # Credits belong in the project landing page and CONTRIBUTORS.md,
    # not repeated in the individual Julia tutorial pages.
    assert "Project contributors:" not in read("Julia/README.md")
    assert "مشارکت‌کنندگان پروژه:" not in read("Julia/README.md")
    assert "Project contributors:" not in read("site_docs/julia/index.en.md")
    assert "مشارکت‌کنندگان پروژه:" not in read("site_docs/julia/index.fa.md")
    assert "مهدیه مقیسه" in read("site_docs/index.fa.md")
    assert "Mahdieh Moghiseh" in read("site_docs/index.en.md")


def test_julia_documentation_is_bilingual_and_in_navigation():
    config = read("mkdocs.yml")
    assert "Julia Learning: julia/index.md" in config
    assert "Julia Learning: آموزش جولیا" in config
    for lang in ("en", "fa"):
        doc = read(f"site_docs/julia/index.{lang}.md")
        for sample in ("01_variables.jl", "04_control_flow.jl", "05_functions.jl"):
            assert sample in doc


def test_existing_exam_review_and_license_still_exist():
    assert (ROOT / "EXAM_NIGHT.md").is_file()
    assert (ROOT / "LICENSE").is_file()
    assert "setup-julia@v2" in read(".github/workflows/julia.yml")
