# -*- coding: utf-8 -*-
"""Public forms."""
from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired


class SearchForm(Form):
    """Search form."""

    query = StringField('Query', validators=[DataRequired()])

    def __init__(self, *args, **kwargs):
        """Create instance."""
        super(SearchForm, self).__init__(*args, **kwargs)
