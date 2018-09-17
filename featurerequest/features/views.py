from flask import render_template,url_for,flash, redirect,request,Blueprint
from featurerequest.features.form import FeatureRequestForm
import featurerequest.database.api as db_api

## Blueprint to register with app
feature_bp = Blueprint('feature_bp',__name__)

## Creates "add_feature" page
@feature_bp.route('/add_feature', methods=['GET', 'POST'])
def add_feature():
    form = FeatureRequestForm()
    if form.validate_on_submit():
        db_api.newFeature(title = form.title.data,
                                  description = form.description.data,
                                  client = form.client.data,
                                  client_priority = form.client_priority.data,
                                  target_date = form.target_date.data,
                                  product_area = form.product_area.data)
        return redirect(url_for('feature_bp.view_feature'))
    return render_template('add_feature.html',form=form)

## Creates "index" page
@feature_bp.route('/')
def index():
    return render_template('index.html')

## Creates "view_feature" page
@feature_bp.route('/view_feature', methods=['GET', 'POST'])
def view_feature():
    features = db_api.queryAll()
    return render_template('view_features.html', features=features)

## Activates the delete button on the view_feature page
@feature_bp.route('/del_feature/<string:id>', methods=['POST'])
def del_feature(id):
    response = db_api.deleteFeature(id)
    if not response == 200: f"Something went wrong trying to delete id #{id}."
    return redirect(url_for('feature_bp.view_feature'))













# @feature_bp.route('/edit_feature/<string:id>', methods=['GET', 'POST'])
# def edit_feature(id):
#     # if request.method == "GET":
#     #     print('Edit-GET')
#     #
#     # if request.method == "POST":
#     #     print('hello')
#     #     feature_to_edit = Feature.query.get(id)
#     #     form = FeatureRequestForm()
#     #     form.title.data = feature_to_edit.title
#     #     form.description.data = feature_to_edit.description
#     #     form.client.data =feature_to_edit.client
#     #     form.client_priority.data =feature_to_edit.client_priority
#     #     form.target_date.data =feature_to_edit.target_date
#     #     form.product_area.data =feature_to_edit.product_area
#     #     form.edit_id.data=id
#     #     print(form)
#
#     # return redirect(url_for('feature_bp.update_feature/'+str(id)))
#
#     return render_template('update_feature.html',form=form)
#
# # @feature_bp.route('/update_feature/<string:id>', methods=['GET', 'POST'])
# # def update_feature(id):
# @feature_bp.route('/update_feature', methods=['GET', 'POST'])
# def update_feature():
#     # print("Why aren't you getting here?")
#     #
#     # form = FeatureRequestForm()
#     # if form.validate_on_submit():
#     #     new_feature = Feature(title = form.title.data,
#     #                               description = form.description.data,
#     #                               client = form.client.data,
#     #                               client_priority = form.client_priority.data,
#     #                               target_date = form.target_date.data,
#     #                               product_area = form.product_area.data)
#     #     db.session.add(new_feature)
#     #     db.session.commit()
#     #     return redirect(url_for('feature_bp.view_feature'))
#     # return render_template('update_feature.html',form=form)
#     # form.edit_id.data =0
#     #
#     # update_this = Feature.query.filter_by(id=id).first()
#     # form = FeatureRequestForm()
#     # if form.validate_on_submit():
#     #     update_this.title=form.title.data
#     #     update_this.description=form.description.data
#     #     update_this.client=form.client.data
#     #     update_this.client_priority=form.client_priority.data
#     #     update_this.target_date=form.target_date.data
#     #     update_this.product_area=form.product_area.data
#     #     db.session.commit()
#     #     return redirect(url_for('feature_bp.view_feature'))
#     # return redirect(url_for('feature_bp.view_feature'))
#
#
#     # return render_template('add_feature.html', form=form)




