import nox

nox.options.env_fallback_enabled = True
nox.options.force_venv_creation = True


@nox.session(python=["3.10", "3.11", "3.12"])
def tests(session):
    session.install("poetry")
    session.run("poetry", "install")
    session.run(
        "pytest",
        "--cov=gpt_engineer",
        "--cov-report=xml",
        "-k",
        "not installed_main_execution",
        env={"OPENAI_API_KEY": session.env.get("OPENAI_API_KEY")},
    )
