import csv
import json

def csv_to_settings(csv_file_path, settings_file_path):
    # Инициализируем структуру JSON на основе предоставленного шаблона
    json_data = {
        "shipping": {
            "installed": {},
            "created": {
                "filterit0": {
                    "title": {"ru-ru": "Страна", "en-gb": "Country"},
                    "status": True,
                    "sort_order": 0,
                    "methods": {},
                    "group_type": "default"
                }
            }
        },
        "payment": {
            "installed": {
                "cod": {
                    "title": {"ru-ru": "Оплата при доставке", "en-gb": "Оплата при доставке"},
                    "description": {"ru-ru": "", "en-gb": ""},
                    "rules": [],
                    "expression": "",
                    "payment_form": {"ru-ru": "", "en-gb": ""},
                    "payment_mail": {"ru-ru": "", "en-gb": ""},
                    "subtotal_texts": {"ru-ru": "", "en-gb": ""},
                    "order_status_id": "",
                    "sort_order": 0,
                    "stub": False,
                    "stub_description": "",
                    "image": "",
                    "image_style": "",
                    "status": {"title": 0, "description": 0, "sort_order": 0, "rules": 0}
                },
                "free_checkout": {
                    "title": {"ru-ru": "Бесплатно", "en-gb": "Бесплатно"},
                    "description": {"ru-ru": "", "en-gb": ""},
                    "rules": [],
                    "expression": "",
                    "payment_form": {"ru-ru": "", "en-gb": ""},
                    "payment_mail": {"ru-ru": "", "en-gb": ""},
                    "subtotal_texts": {"ru-ru": "", "en-gb": ""},
                    "order_status_id": "",
                    "sort_order": 0,
                    "stub": False,
                    "stub_description": "",
                    "image": "",
                    "image_style": "",
                    "status": {"title": 0, "description": 0, "sort_order": 0, "rules": 0}
                },
                "assist": {
                    "title": {"ru-ru": "ASSIST - провайдер электронных платежей ", "en-gb": "ASSIST - провайдер электронных платежей "},
                    "description": {"ru-ru": "", "en-gb": ""},
                    "rules": [],
                    "expression": "",
                    "payment_form": {"ru-ru": "", "en-gb": ""},
                    "payment_mail": {"ru-ru": "", "en-gb": ""},
                    "subtotal_texts": {"ru-ru": "", "en-gb": ""},
                    "order_status_id": "",
                    "sort_order": 0,
                    "stub": False,
                    "stub_description": "",
                    "image": "",
                    "image_style": "",
                    "status": {"title": 0, "description": 0, "sort_order": 0, "rules": 0}
                },
                "webpay_card": {
                    "title": {"ru-ru": "Webpay Payments / Оплата картой", "en-gb": "Webpay Payments / Оплата картой"},
                    "description": {"ru-ru": "", "en-gb": ""},
                    "rules": [],
                    "expression": "",
                    "payment_form": {"ru-ru": "", "en-gb": ""},
                    "payment_mail": {"ru-ru": "", "en-gb": ""},
                    "subtotal_texts": {"ru-ru": "", "en-gb": ""},
                    "order_status_id": "",
                    "sort_order": 0,
                    "stub": False,
                    "stub_description": "",
                    "image": "",
                    "image_style": "",
                    "status": {"title": 0, "description": 0, "sort_order": 0, "rules": 0}
                }
            },
            "created": {}
        },
        "sort_order": "8",
        "status": "1"
    }

    # Читаем CSV файл
    with open(csv_file_path, 'r', encoding='windows-1251') as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=";")
        for index, row in enumerate(csv_reader):
            method_key = f"filterit{index}"
            json_data["shipping"]["created"]["filterit0"]["methods"][method_key] = {
                "title": {
                    "ru-ru": f"{row['description_ru']}",
                    "en-gb": f"{row['description_en']}"
                },
                "description": {
                    "ru-ru": f"{row['description_ru']}",
                    "en-gb": f"{row['description_en']}"
                },
                "rules": {
                    "$0": {
                        "field": f"{row['identifier_name']}",
                        "item": "",
                        "compare": "equal",
                        "value": "",
                        "values": [row['identifier_id']]
                    }
                },
                "expression": "",
                "status": True,
                "cost": row['delivery_cost'],
                "cost_text": "",
                "cost_type": "1",
                "cost_table": [],
                "stub": False,
                "stub_description": "",
                "tax_class_id": "",
                "image": "",
                "image_style": "",
                "sort_order": 0,
                "currency": "USD"
            }

    # Записываем данные в файл .settings
    with open(settings_file_path, 'w', encoding='utf-8') as settings_file:
        json.dump(json_data, settings_file, ensure_ascii=False, separators=(',', ':'))

# Пример использования
csv_file_path = 'Countries_and_cities.csv'
settings_file_path = 'filterit.setting'
csv_to_settings(csv_file_path, settings_file_path)
print(f".settings файл успешно создан: {settings_file_path}")