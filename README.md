### Hexlet tests and linter status:
[![Actions Status](https://github.com/Anatoliy2610/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/Anatoliy2610/python-project-50/actions)

[![Maintainability](https://api.codeclimate.com/v1/badges/6798f68cade64214cb0f/maintainability)](https://codeclimate.com/github/Anatoliy2610/python-project-50/maintainability)

[![Test Coverage](https://api.codeclimate.com/v1/badges/6798f68cade64214cb0f/test_coverage)](https://codeclimate.com/github/Anatoliy2610/python-project-50/test_coverage)

# Вычислитель отличий
1. проект представляет собой программу, которая определяет разницу между двумя структурами данных.
2. установить проект себе можно прописав команды в командной строке:
- `git clone https://github.com/Anatoliy2610/python-project-50?tab=readme-ov-file`
- `make build`
- `make publish`
- `make package-install`
3. пример работы программы:
- `gendiff tests/fixtures/file1.json tests/fixtures/file2.json` - сравнение двух плоских файлов формата json
- `gendiff tests/fixtures/file1.yaml tests/fixtures/file2.yaml` - сравнение двух плоских файлов формата yaml или yml
- `gendiff tests/fixtures/file3.json tests/fixtures/file4.json` или `gendiff tests/fixtures/file3.yaml tests/fixtures/file4.jyaml` - сравнение двух файлов, имеющие вложенную структуру формата json или yaml
- `gendiff --format plain tests/fixtures/file3.json tests/fixtures/file4.json` - сравнение двух файлов, вывод которых осуществляется в формате plain
- `gendiff --format json tests/fixtures/file3.json tests/fixtures/file4.json` - сравнение двух файлов, вывод которых осуществляется в формате json
**Видео:**
[![asciicast](https://asciinema.org/a/tSxccgAsHLbELPbfxyOgGF1De.svg)](https://asciinema.org/a/tSxccgAsHLbELPbfxyOgGF1De)
