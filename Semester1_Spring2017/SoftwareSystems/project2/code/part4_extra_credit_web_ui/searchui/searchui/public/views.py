# -*- coding: utf-8 -*-
"""Public section, including homepage and signup."""
import json

from flask import Blueprint, flash, redirect, render_template, request, url_for

from searchui.public.forms import SearchForm
from searchui.utils import flash_errors
from searchui.query import index
from searchui.query import query as search_index

blueprint = Blueprint('public', __name__, static_folder='../static')


@blueprint.route('/', methods=['GET', 'POST'])
def home():
    """Home page."""
    form = SearchForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            query = json.dumps({"query": str(form.query.data)})
            redirect_url = url_for('public.search_results', query=query)
            return redirect(redirect_url)
        else:
            flash_errors(form)
    return render_template('public/home.html', form=form)


@blueprint.route('/results')
def search_results():
    """Search results page."""
    query = request.args['query']
    results = search_index(query)
    if results is None:
        return render_template('public/search_results.html')
    # results = [{"word": "test", "doc_name": "test", "line_number": "test", "word_number": "test"}, {"word": "test2", "doc_name": "test", "line_number": "test", "word_number": "test"}]
    return render_template('public/search_results.html', results=results)


@blueprint.route('/about/')
def about():
    """About page."""
    return render_template('public/about.html')
