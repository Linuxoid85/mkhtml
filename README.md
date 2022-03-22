# mkhtml - Make HTML.

Скрипт для генерации HTML-страниц из Markdown документов. Предназначено для работы в репозитории [linuxoid85.github.io](https://github.com/Linuxoid85/linuxoid85.github.io).

> **ВНИМАНИЕ!**

> Это не генератор документации по типу `mkdocs`, `sphinx` или `docsify`.

## Особенности

- Простая конфигурация в `JSON` файле
- Генерация страниц с простым форматированием. Я считаю, что главное - не красота, а простой доступ к информации.
- Автогенерация содержания документа.

## TODO

- [ ] **Возможность управления расширениями.** Сейчас невозможно изменить список расширений `markdown`, не отредактировав исходный код [`libmkhtml`](src/libmkhtml.py). Предлагается вынести список расширений в json-конфиг скрипта.
- [ ] Добавить подсветку синтаксиса в блоках кода.
- [ ] Убрать генерацию `tags[1]` для `/README.md`.
- [ ] Из страниц `README.md` генерировать не `README.html`, а `index.html`.
- [ ] Вынести определение значения `tags[1]` из исходного кода `libmkhtml`. Как значение подставлять HTML-теги, взятые из отдельного файла.

## Использование

Поместить исходный код из директории `src/` в директорию со страницами. Описать все необходимые для генерации страницы в json-конфиге. Название страниц указывать **без** расширения.