# Developer README

## Contributing
The project uses: -

- [pre-commit] to enforce linting of files prior to committing them to the
  upstream repository
- [Commitizen] to enforce a [Conventional Commit] commit message format

You **MUST** comply with these choices in order to  contribute to the project.

To get started review the pre-commit utility and the conventional commit style
and then setup your local clone by following the **Installation** and
**Quick Start** sections: -

    pip install -r build-requirements.txt
    pre-commit install -t commit-msg -t pre-commit

Now the project's rules will run on every commit, and you can check the
current health of your clone with: -

    pre-commit run --all-files

Create a virtual environment if you're going to develop code.

## Building
It's a standard Python package, controlled by `setup.py` so familiarity
with [Python packaging] will help. The project is built and published
to PyPI automatically from the main branch using GitHub Actions.

To build the package distribution manually you will need to have
[protoc] installed, you can then run: -

```bash
export P_BASE=src/main/proto
export I_PATH=informaticsmatters/protobuf

for P_DIR in $(ls -d ${P_BASE}/${I_PATH}/*/); do
    protoc -I=${P_BASE} --python_out=${P_BASE} ${P_DIR}/*.proto;
    touch ${P_DIR}/__init__.py
done
touch ${P_BASE}/${I_PATH}/__init__.py

python -m pip install --upgrade build
python -m build --sdist --wheel --outdir dist/
```

>   Because you're building outside the CI process the version number of
    the package will be fixed at 2.0.0. DO NOT change this behaviour.

To install the local build, without needing to publish the package run: -

    pip install dist/im_protobuf-2.0.0-py3-none-any.whl

---

[commitizen]: https://commitizen-tools.github.io/commitizen/
[conventional commit]: https://www.conventionalcommits.org/en/v1.0.0/
[pre-commit]: https://pre-commit.com
[protoc]: https://github.com/protocolbuffers/protobuf
[python packaging]: https://packaging.python.org/en/latest/tutorials/packaging-projects/
