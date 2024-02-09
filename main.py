from repositories.note_repository import NoteRepository
from services.note_service import NoteService

def main():
    note_repository = NoteRepository("notes.json")
    note_service = NoteService(note_repository)

    while True:
        print("Доступные команды:")
        print("1. Добавить заметку")
        print("2. Список заметок")
        print("3. Редактировать заметку")
        print("4. Удалить заметку")
        print("5. Выборка заметок по дате")
        print("6. Выйти")

        choice = input("Введите номер команды: ")

        if choice == "1":
            title = input("Введите заголовок заметки: ")
            message = input("Введите тело заметки: ")
            note_service.add_note(title, message)
        elif choice == "2":
            notes = note_service.list_notes()
            if notes:
                for note in notes:
                    print(note)
            else:
                print("Заметок пока нет.")
        elif choice == "3":
            note_id = int(input("Введите ID заметки для редактирования: "))
            title = input("Введите новый заголовок заметки: ")
            message = input("Введите новое тело заметки: ")
            edited_note = note_service.edit_note(note_id, title, message)
            if edited_note:
                print(f"Заметка успешно отредактирована: {edited_note}")
            else:
                print("Заметка с указанным ID не найдена.")
        elif choice == "4":
            note_id = int(input("Введите ID заметки для удаления: "))
            if note_service.delete_note(note_id):
                print("Заметка успешно удалена.")
            else:
                print("Заметка с указанным ID не найдена.")
        elif choice == "5":
            date = input("Введите дату для выборки заметок (гггг-мм-дд): ")
            filtered_notes = note_service.filter_notes_by_date(date)
            if filtered_notes:
                for note in filtered_notes:
                    print(note)
            else:
                print("Заметок за указанную дату не найдено.")
        elif choice == "6":
            print("Выход из программы.")
            break
        else:
            print("Некорректный ввод. Пожалуйста, введите число от 1 до 6.")

if __name__ == "__main__":
    main()
