# API Reference

## `parse_notation(notation: str) -> tuple[int, int, int]`

Разбирает строку формата `XdY(+|-)Z` и возвращает количество кубиков,
число граней и модификатор.

## `roll_once(count: int, sides: int, mod: int) -> RollResult`

Выполняет один бросок указанного количества кубиков и возвращает сумму,
список значений и применённый модификатор.

## `create_histogram(results: Iterable[int], path: str) -> None`

Строит гистограмму из последовательности результатов и сохраняет в PNG-файл.

## `cli.main(argv: Sequence[str] | None) -> None`

Точка входа командной утилиты. Обрабатывает аргументы и выводит результат на
экран.
