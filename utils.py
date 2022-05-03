"""load_candidates_from_json(path)` – возвращает список всех кандидатов
    get_candidate(candidate_id)` – возвращает одного кандидата по его id
    get_candidates_by_name(candidate_name)` – возвращает кандидатов по имени
    get_candidates_by_skill(skill_name)` – возвращает кандидатов по навыку"""

import json


def load_candidates_from_json(path):
    with open(path, "r", encoding="UTF-8") as file:
        return json.load(file)


def get_candidate(candidate_id):
    candidates = load_candidates_from_json("candidates.json")
    for candidate in candidates:
        if candidate["id"] == candidate_id:
            return candidate
    return None


def get_candidates_by_name(candidate_name):
    candidates = load_candidates_from_json("candidates.json")
    candidates_with_same_names = []
    for candidate in candidates:
        if candidate_name.lower() in candidate["name"].lower():
            candidates_with_same_names.append(candidate)

    return candidates_with_same_names


def get_candidates_by_skill(skill_name):
    candidates = load_candidates_from_json("candidates.json")
    candidates_with_same_skills = []
    for candidate in candidates:
        if skill_name.lower() in candidate["skills"].lower():
            candidates_with_same_skills.append(candidate)

    return candidates_with_same_skills

