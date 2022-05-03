from flask import Flask, render_template, abort

import utils

app = Flask(__name__)


@app.route("/")
def list_candidates():
    candidates = utils.load_candidates_from_json("candidates.json")
    return render_template("list.html", candidates=candidates)


@app.route("/candidate/<int:candidate_id>")
def print_candidate_by_id(candidate_id):
    candidate = utils.get_candidate(candidate_id)
    if candidate:
        return render_template("card.html", candidate=candidate)
    abort(404)


@app.route("/search/<string:candidate_name>")
def print_candidates_by_name(candidate_name):
    candidates = utils.get_candidates_by_name(candidate_name)
    return render_template("search.html", candidates=candidates, candidates_count=len(candidates))


@app.route("/skill/<string:skill_name>")
def print_candidates_by_skills(skill_name):
    candidates = utils.get_candidates_by_skill(skill_name)
    return render_template("skill.html", candidates=candidates, candidates_count=len(candidates))


app.run(port=5004)