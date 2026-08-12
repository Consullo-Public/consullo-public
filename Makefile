.PHONY: assets build verify

build:
	python3 tools/build.py

verify:
	python3 tools/verify_public.py

assets:
	@echo "Pass the approved source explicitly: python3 tools/derive_logo.py --source PATH"

