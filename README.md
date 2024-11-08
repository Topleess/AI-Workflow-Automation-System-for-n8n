# AI-Workflow-Automation-System-for-n8n

**AI Workflow Automation System for n8n** — это Python-приложение, предназначенное для автоматизации создания и управления рабочими процессами (workflow) на платформе **n8n** с использованием искусственного интеллекта. Система использует многоагентную архитектуру, где каждый агент выполняет определённые задачи: от анализа запроса пользователя до создания и тестирования workflow, обеспечивая автоматизацию процессов без необходимости глубоких технических знаний.

## Цель проекта

Проект создан для автоматизации и упрощения работы с n8n. С помощью AI-агентов пользователи смогут описывать задачи на естественном языке, а система предложит готовый workflow, состоящий из нод n8n, или сгенерирует необходимые кастомные ноды.

## Структура проекта

- `project/`
  - `app/` - Основное приложение
    - `agents/` - Папка для хранения отдельных агентов, каждый агент в своём модуле
      - `user_interaction.py` - Агент для взаимодействия с пользователем
      - `resource_search.py` - Агент для поиска ресурсов и нод
      - `code_generation.py` - Агент для генерации кода и нод
      - `testing.py` - Агент для тестирования и валидации
    - `api/` - Эндпоинты для взаимодействия с приложением
      - `main.py` - Основной эндпоинт API (например, на FastAPI)
    - `models/` - Модели для работы через API (поддержка self-hosted и удалённых моделей)
      - `model_manager.py` - Менеджер для универсального доступа к моделям
      - `self_hosted/` - Папка для локально развернутых моделей
      - `remote/` - Папка для интеграции с удалёнными моделями (например, OpenAI API)
    - `workflows/` - Логика создания и управления workflow
      - `workflow_builder.py` - Модуль для сборки workflow из нод
    - `validators/` - Модуль для генерации, тестирования и передачи кода
      - `code_validator.py` - Скрипт, проверяющий корректность кода (работает или не работает)
      - `code_generator.py` - Генерация кода для выполнения
      - `executor.py` - Скрипт для исполнения сгенерированного кода и сбора результата
    - `utils/` - Вспомогательные утилиты для общих задач
  - `config/` - Настройки и параметры конфигурации для проекта
    - `settings.py` - Основные параметры (например, ключи API, настройки моделей)
  - `requirements.txt` - Зависимости проекта
  - `tests/` - Тесты для различных частей системы
    - `test_agents/` - Тесты для агентов
    - `test_models/` - Тесты для моделей и их универсального доступа
    - `test_validators/` - Тесты для валидации и генерации кода
    - `test_workflows/` - Тесты для workflow-сборки и API-интеграции
  - `main.py` - Точка входа в приложение


## Основные функции

1. **Анализ запроса пользователя** — ИИ-агент принимает описание задачи на естественном языке и разбивает её на подзадачи.
2. **Поиск и настройка нод n8n** — автоматический поиск и конфигурация нод в n8n, необходимых для выполнения задач.
3. **Создание кастомных нод** — если требуемая нода отсутствует, агент предлагает создать её либо с использованием существующих API, либо написанием кода.
4. **Тестирование и валидация** — автоматическое тестирование workflow и проверка корректности выполнения.
5. **Информирование и поддержка** — уведомление пользователя о результатах работы и предложение тестового запуска.
6. **Обеспечение безопасности** — проверка безопасности и оптимизация для надёжной работы.

## Примеры использования

### Пример 1: Уведомления в Telegram при новых заявках

1. **Пользователь:** "Хочу получать уведомление в Telegram, когда на мой сайт поступает новая заявка."
2. **Агент:**
   - Анализирует задачу и предлагает план действий: отслеживание заявок на сайте, получение данных о заявке, отправка уведомления в Telegram.
   - Проверяет наличие необходимых нод в n8n и создаёт workflow, состоящий из этих нод.
   - Проводит тестирование и сообщает о результатах.

### Пример 2: Автоматическая публикация статей в Twitter

1. **Пользователь:** "Я хочу автоматически публиковать новые статьи с моего блога в Twitter."
2. **Агент:**
   - Предлагает план: отслеживание новых статей через RSS или API, публикация ссылок в Twitter.
   - Проверяет доступные ноды n8n и создаёт кастомную ноду, если нужная нода отсутствует.
   - Информирует пользователя о статусе и готовности workflow.

## Планы по доработке

1. **Поддержка интерфейса для управления нодами и workflow** — возможность визуально управлять нодами и их конфигурацией.
2. **Интеграция с Figma и n8n** — для конвертации дизайнов из Figma в UI-компоненты и ноды из n8n в код.
3. **AI-конструктор прототипов** — автоматическое создание проекта на основе макетов и описаний, с поддержкой уточнения данных и функций.
4. **Логическое тестирование** — добавление тестов для проверки корректности данных на каждом этапе выполнения workflow.

## Перспективы и связи с n8n

**AI Workflow Automation System for n8n** помогает автоматизировать процесс работы с n8n, облегчая переход между визуальным программированием и редактированием кода. Это позволяет использовать систему как для нетехнических пользователей, которые могут создавать автоматизации с помощью нод, так и для разработчиков, которые смогут дорабатывать код и переносить его обратно в n8n.

## Лицензия

Этот проект лицензирован под MIT License.

## Приложение
Создано с помощью автогереатора папок [(ссылка)](https://github.com/Topleess/ai-project-structure-generator)
