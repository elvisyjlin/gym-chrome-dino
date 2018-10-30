# clean the build directory
clean:
	rm -rf build/ dist/ .eggs/ *.egg-info/ || true

# build the deployment package
deploy: clean
	python3 setup.py sdist bdist_wheel --universal

# ship the deployment package to PyPI
ship: deploy
	twine upload dist/*
