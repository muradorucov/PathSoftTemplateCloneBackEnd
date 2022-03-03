from app import app
from app.models import*
from admin.forms import*
from app import db
import os
import random
from flask import Flask,redirect,url_for,render_template,request
from werkzeug.utils import secure_filename
from datetime import date
today = date.today()

@app.route("/admin/")
def admin_index():
    contactforms=ContactForm.query.all()
    usercomments=UserComment.query.all()
    return render_template("admin/index.html",usercomments=usercomments, contactforms=contactforms)


# Header Contact Info start
@app.route("/admin/hcContactAdd/", methods=['GET','POST'])
def hcContactAdd():
    form=HeaderContactForm()
    header_contacts=HeaderContact.query.all()
    if request.method=='POST':
        header_contact=HeaderContact(
            hc_content=form.hc_content.data,
            hc_icon_class=form.hc_icon_class.data,
            hc_url=form.hc_url.data
        )
        db.session.add(header_contact)
        db.session.commit()
        return redirect(url_for('hcContactAdd'))
    return render_template("admin/hcContactAdd.html", form=form, header_contacts=header_contacts)

@app.route("/admin/hcContactUpdate/<id>",methods=['GET','POST'])
def hcContactUpdate(id):
    header_contact=HeaderContact.query.get(id)
    form=HeaderContactForm()
    if request.method=='POST':
        header_contact.hc_content=form.hc_content.data
        header_contact.hc_icon_class=form.hc_icon_class.data
        header_contact.hc_url=form.hc_url.data
        db.session.commit()
        return redirect(url_for('hcContactAdd'))
    return render_template('admin/hcContactUpdate.html',form=form, header_contact=header_contact)

@app.route("/admin/hcContactDelete/<id>")
def hcContactDelete(id):
    header_contact=HeaderContact.query.get(id)
    db.session.delete(header_contact)
    db.session.commit()
    return redirect(url_for('hcContactAdd'))
# Header Contact Info end



# Header Social icon start
@app.route("/admin/headerSocialIconAdd/", methods=['GET','POST'])
def headerSocialIconAdd():
    form=HeaderSocialIconForm()
    headersocial_icons=HeaderSocialIcon.query.all()
    if request.method=='POST':
        headersocial_icon=HeaderSocialIcon(
            hsi_name=form.hsi_name.data,
            hsi_css_class=form.hsi_css_class.data,
            hsi_url=form.hsi_url.data
        )
        db.session.add(headersocial_icon)
        db.session.commit()
        return redirect(url_for('headerSocialIconAdd'))
    return render_template("admin/headerSocialIconAdd.html",form=form, headersocial_icons=headersocial_icons)

@app.route("/admin/headerSocialIconUpdate/<id>",methods=['GET','POST'])
def headerSocialIconUpdate(id):
    form=HeaderSocialIconForm()
    headersocial_icon=HeaderSocialIcon.query.get(id)
    if request.method=='POST':
        headersocial_icon.hsi_name=form.hsi_name.data
        headersocial_icon.hsi_css_class=form.hsi_css_class.data
        headersocial_icon.hsi_url=form.hsi_url.data
        db.session.commit()
        return redirect(url_for('headerSocialIconAdd'))
    return render_template('admin/headerSocialIconUpdate.html',form=form, headersocial_icon=headersocial_icon)

@app.route("/admin/headerSocialIconDelete/<id>")
def headerSocialIconDelete(id):
    headersocial_icon=HeaderSocialIcon.query.get(id)
    db.session.delete(headersocial_icon)
    db.session.commit()
    return redirect(url_for('headerSocialIconAdd'))
# Header Socila icon End



# Header Meniu Logo start
@app.route("/admin/meniuLogoAdd", methods=['GET','POST'])
def meniuLogoAdd():
    form=MeniuLogoForm()
    logos=MeniuLogo.query.all()
    if request.method=='POST':
        file=form.logo_img.data
        logo_name=file.filename
        randomlogo=random.randint(0,599)
        logo_title= secure_filename(form.logo_title.data)
        logo_extention=logo_name.split(".")[-1]
        logoName=logo_title+str(randomlogo)+ '.' + logo_extention
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], logoName))
        logo=MeniuLogo(
            logo_title=form.logo_title.data,
            logo_url=form.logo_url.data,
            logo_alt=form.logo_alt.data,
            logo_img=logoName
        )
        db.session.add(logo)
        db.session.commit()
        return redirect(url_for('meniuLogoAdd'))
    return render_template("admin/meniuLogoAdd.html", form=form, logos=logos)

@app.route("/admin/meniuLogoUpdate/<id>",methods=['GET','POST'])
def meniuLogoUpdate(id):
    form=MeniuLogoForm()
    logo=MeniuLogo.query.get(id)
    if request.method=='POST':
        file=form.logo_img.data
        logo_name=file.filename
        randomlogo=random.randint(0,599)
        logo_title= secure_filename(form.logo_title.data)
        logo_extention=logo_name.split(".")[-1]
        logoName=logo_title+str(randomlogo)+ '.' + logo_extention
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], logoName))
        logo.logo_title=form.logo_title.data
        logo.logo_url=form.logo_url.data
        logo.logo_alt=form.logo_alt.data
        logo.logo_img=logoName
        db.session.commit()
        return redirect(url_for('meniuLogoAdd'))
    return render_template('admin/meniuLogoUpdate.html',form=form, logo=logo)

@app.route("/admin/meniuLogoDelete/<id>")
def meniuLogoDelete(id):
    logos=MeniuLogo.query.get(id)
    db.session.delete(logos)
    db.session.commit()
    return redirect(url_for('meniuLogoAdd'))
# Header Meniu Logo end



# Header Meniu Name start
@app.route("/admin/meniuNameAdd", methods=['GET','POST'])
def meniuNameAdd():
    form=MeniuNameForm()
    meniu_names=MeniuName.query.all()
    if request.method=='POST':
        meniu_name=MeniuName(
            meniu_title=form.meniu_title.data,
            meniu_url=form.meniu_url.data,
            meniu_icon=form.meniu_icon.data
        )
        db.session.add(meniu_name)
        db.session.commit()
        return redirect(url_for('meniuNameAdd'))
    return render_template("admin/meniuNameAdd.html",form=form, meniu_names=meniu_names)

@app.route("/admin/meniuNameUpdate/<id>",methods=['GET','POST'])
def meniuNameUpdate(id):
    form=MeniuNameForm()
    meniu_name=MeniuName.query.get(id)
    if request.method=='POST':
        meniu_name.meniu_title=form.meniu_title.data
        meniu_name.meniu_url=form.meniu_url.data
        meniu_name.meniu_icon=form.meniu_icon.data
        db.session.commit()
        return redirect(url_for('meniuNameAdd'))
    return render_template('admin/meniuNameUpdate.html',form=form, meniu_name=meniu_name)

@app.route("/admin/meniuNameDelete/<id>")
def meniuNameDelete(id):
    meniu_name=MeniuName.query.get(id)
    db.session.delete(meniu_name)
    db.session.commit()
    return redirect(url_for('meniuNameAdd'))
# Header Meniu Name end


# Slider Image Start
@app.route("/admin/sliderImageAdd/", methods=['GET','POST'])
def sliderImageAdd():
    form=SliderForm()
    sliders=Slider.query.all()
    if request.method=='POST':
        file=form.slider_img.data
        slider_img_name=file.filename
        randomslider=random.randint(600,1678)
        slider_alt= secure_filename(form.slider_alt.data)
        slider_extention=slider_img_name.split(".")[-1]
        sliderImg=slider_alt+ str(randomslider)+"."+slider_extention
        file.save(os.path.join(app.config['UPLOAD_FOLDER'],sliderImg))
        slider=Slider(
            slider_title=form.slider_title.data,
            slider_text=form.slider_text.data,
            slider_alt=form.slider_alt.data,
            slider_img=sliderImg
        )
        db.session.add(slider)
        db.session.commit()
        return redirect(url_for('sliderImageAdd'))
    return render_template("admin/sliderImageAdd.html",form=form, sliders=sliders)

@app.route("/admin/sliderImageUpdate/<id>",methods=['GET','POST'])
def sliderImageUpdate(id):
    form=SliderForm()
    slider=Slider.query.get(id)
    if request.method=='POST':
        file=form.slider_img.data
        slider_img_name=file.filename
        randomslider=random.randint(600,1678)
        slider_alt= secure_filename(form.slider_alt.data)
        slider_extention=slider_img_name.split(".")[-1]
        sliderImg=slider_alt+ str(randomslider)+"."+slider_extention
        file.save(os.path.join(app.config['UPLOAD_FOLDER'],sliderImg))
        slider.slider_title=form.slider_title.data
        slider.slider_text=form.slider_text.data
        slider.slider_alt=form.slider_alt.data
        slider.slider_img=sliderImg
        db.session.commit()
        return redirect(url_for('sliderImageAdd'))
    return render_template('admin/sliderImageUpdate.html',form=form, slider=slider)

@app.route("/admin/sliderImageDelete/<id>")
def sliderImageDelete(id):
    slider=Slider.query.get(id)
    db.session.delete(slider)
    db.session.commit()
    return redirect(url_for('sliderImageAdd'))
# Slider Image End



# Slider Button Start
@app.route("/admin/sliderBttnAdd", methods=['GET','POST'])
def sliderBttnAdd():
    form=SliderUrlForm()
    sliderbttns=SliderUrl.query.all()
    if request.method=='POST':
        sliderbttn=SliderUrl(
            sliderurl_title=form.sliderurl_title.data,
            sliderurl_icon=form.sliderurl_icon.data,
            sliderurl_url=form.sliderurl_url.data
        )
        db.session.add(sliderbttn)
        db.session.commit()
        return redirect(url_for('sliderBttnAdd'))
    return render_template("admin/sliderBttnAdd.html",form=form, sliderbttns=sliderbttns)

@app.route("/admin/sliderBttnUpdate/<id>",methods=['GET','POST'])
def sliderBttnUpdate(id):
    form=SliderUrlForm()
    sliderbttn=SliderUrl.query.get(id)
    if request.method=='POST':
        sliderbttn.sliderurl_title=form.sliderurl_title.data
        sliderbttn.sliderurl_icon=form.sliderurl_icon.data
        sliderbttn.sliderurl_url=form.sliderurl_url.data
        db.session.commit()
        return redirect(url_for('sliderBttnAdd'))
    return render_template('admin/sliderBttnUpdate.html',form=form, sliderbttn=sliderbttn)

@app.route("/admin/sliderBttnDelete/<id>")
def sliderBttnDelete(id):
    sliderbttn=SliderUrl.query.get(id)
    db.session.delete(sliderbttn)
    db.session.commit()
    return redirect(url_for('sliderBttnAdd'))
# Slider Button End




# Service Heading Start
@app.route("/admin/serviceHeadingAdd", methods=['GET','POST'])
def serviceHeadingAdd():
    form=ServiceTitleForm()
    serviceheadings=ServiceTitle.query.all()
    if request.method=='POST':
        serviceheading=ServiceTitle(
            service_subheading=form.service_subheading.data,
            service_title=form.service_title.data
        )
        db.session.add(serviceheading)
        db.session.commit()
        return redirect(url_for('serviceHeadingAdd'))
    return render_template("admin/serviceHeadingAdd.html",form=form, serviceheadings=serviceheadings)

@app.route("/admin/serviceHeadingUpdate/<id>",methods=['GET','POST'])
def serviceHeadingUpdate(id):
    form=ServiceTitleForm()
    serviceheading=ServiceTitle.query.get(id)
    if request.method=='POST':
        serviceheading.service_subheading=form.service_subheading.data
        serviceheading.service_title=form.service_title.data
        db.session.commit()
        return redirect(url_for('serviceHeadingAdd'))
    return render_template('admin/serviceHeadingUpdate.html',form=form, serviceheading=serviceheading)

@app.route("/admin/serviceHeadingDelete/<id>")
def serviceHeadingDelete(id):
    serviceheading=ServiceTitle.query.get(id)
    db.session.delete(serviceheading)
    db.session.commit()
    return redirect(url_for('serviceHeadingAdd'))
# Service Heading End



# Service Item start
@app.route("/admin/serviceItemAdd", methods=['GET','POST'])
def serviceItemAdd():
    form=ServiceItemForm()
    serviceitems=ServiceItem.query.all()
    if request.method=='POST':
        serviceitem=ServiceItem(
            servitem_title=form.servitem_title.data,
            servitem_text=form.servitem_text.data,
            servitem_url=form.servitem_url.data,
            servitem_icon=form.servitem_icon.data
        )
        db.session.add(serviceitem)
        db.session.commit()
        return redirect(url_for('serviceItemAdd'))
    return render_template("admin/serviceItemAdd.html",form=form, serviceitems=serviceitems)

@app.route("/admin/serviceItemUpdate/<id>",methods=['GET','POST'])
def serviceItemUpdate(id):
    form=ServiceItemForm()
    serviceitem=ServiceItem.query.get(id)
    if request.method=='POST':
        serviceitem.servitem_title=form.servitem_title.data
        serviceitem.servitem_text=form.servitem_text.data
        serviceitem.servitem_url=form.servitem_url.data
        serviceitem.servitem_icon=form.servitem_icon.data
        db.session.commit()
        return redirect(url_for('serviceItemAdd'))
    return render_template('admin/serviceItemUpdate.html',form=form, serviceitem=serviceitem)

@app.route("/admin/serviceItemDelete/<id>")
def serviceItemDelete(id):
    serviceitem=ServiceItem.query.get(id)
    db.session.delete(serviceitem)
    db.session.commit()
    return redirect(url_for('serviceItemAdd'))
# Service Item End



# Service Button start
@app.route("/admin/serviceBttnAdd", methods=['GET', 'POST'])
def serviceBttnAdd():
    form=ServiceButtonForm()
    servicebttns=ServiceButton.query.all()
    if request.method== "POST":
        servicebttn=ServiceButton(
            servbttn_title=form.servbttn_title.data,
            servbttn_icon=form.servbttn_icon.data,
            servbttn_url=form.servbttn_url.data
        )
        db.session.add(servicebttn)
        db.session.commit()
        return redirect(url_for('serviceBttnAdd'))
    return render_template('admin/serviceBttnAdd.html',form=form, servicebttns=servicebttns)

@app.route("/admin/serviceBttnUpdate/<id>", methods=['GET','POST'])
def serviceBttnUpdate(id):
    form=ServiceButtonForm()
    servicebttn=ServiceButton.query.get(id)
    if request.method=='POST':
        servicebttn.servbttn_title=form.servbttn_title.data
        servicebttn.servbttn_icon=form.servbttn_icon.data
        servicebttn.servbttn_url=form.servbttn_url.data
        db.session.commit()
        return redirect(url_for('serviceBttnAdd'))
    return render_template('admin/serviceBttnUpdate.html',form=form, servicebttn=servicebttn)

@app.route("/admin/serviceBttnDelete/<id>")
def serviceBttnDelete(id):
    servicebttn=ServiceButton.query.get(id)
    db.session.delete(servicebttn)
    db.session.commit()
    return redirect(url_for('serviceBttnAdd'))
# Service Button end



# Reason Heading start
@app.route("/admin/reasonHeadingAdd", methods=['GET', 'POST'])
def reasonHeadingAdd():
    form=ReasonTitleForm()
    reasonheadings=ReasonTitle.query.all()
    if request.method== "POST":
        reasonheading=ReasonTitle(
            reason_subheading=form.reason_subheading.data,
            reason_title=form.reason_title.data
        )
        db.session.add(reasonheading)
        db.session.commit()
        return redirect(url_for('reasonHeadingAdd'))
    return render_template('admin/reasonHeadingAdd.html',form=form, reasonheadings=reasonheadings)

@app.route("/admin/reasonHeadingUpdate/<id>", methods=['GET','POST'])
def reasonHeadingUpdate(id):
    form=ReasonTitleForm()
    reasonheading=ReasonTitle.query.get(id)
    if request.method=='POST':
        reasonheading.reason_subheading=form.reason_subheading.data
        reasonheading.reason_title=form.reason_title.data
        db.session.commit()
        return redirect(url_for('reasonHeadingAdd'))
    return render_template('admin/reasonHeadingUpdate.html',form=form, reasonheading=reasonheading)

@app.route("/admin/reasonHeadingDelete/<id>")
def reasonHeadingDelete(id):
    reasonheading=ReasonTitle.query.get(id)
    db.session.delete(reasonheading)
    db.session.commit()
    return redirect(url_for('reasonHeadingAdd'))
# Reason Heading end



# Reason Item start
@app.route("/admin/reasonItemAdd", methods=['GET', 'POST'])
def reasonItemAdd():
    form=ReasonItemForm()
    reasonitems=ReasonItem.query.all()
    if request.method== "POST":
        reasonitem=ReasonItem(
            reasonitem_number=form.reasonitem_number.data,
            reasonitem_title=form.reasonitem_title.data,
            reasonitem_text=form.reasonitem_text.data
        )
        db.session.add(reasonitem)
        db.session.commit()
        return redirect(url_for('reasonItemAdd'))
    return render_template('admin/reasonItemAdd.html',form=form, reasonitems=reasonitems)

@app.route("/admin/reasonItemUpdate/<id>", methods=['GET','POST'])
def reasonItemUpdate(id):
    form=ReasonItemForm()
    reasonitem=ReasonItem.query.get(id)
    if request.method=='POST':
        reasonitem.reasonitem_number=form.reasonitem_number.data
        reasonitem.reasonitem_title=form.reasonitem_title.data
        reasonitem.reasonitem_text=form.reasonitem_text.data
        db.session.commit()
        return redirect(url_for('reasonItemAdd'))
    return render_template('admin/reasonItemUpdate.html',form=form, reasonitem=reasonitem)

@app.route("/admin/reasonItemDelete/<id>")
def reasonItemDelete(id):
    reasonitem=ReasonItem.query.get(id)
    db.session.delete(reasonitem)
    db.session.commit()
    return redirect(url_for('reasonItemAdd'))
# Reason Item end



# Project Heading start
@app.route("/admin/projectHeadingAdd", methods=['GET', 'POST'])
def projectHeadingAdd():
    form=ProjectHeaderForm()
    projectheadings=ProjectHeader.query.all()
    if request.method== "POST":
        projectheading=ProjectHeader(
            project_subheading=form.project_subheading.data,
            project_title=form.project_title.data
        )
        db.session.add(projectheading)
        db.session.commit()
        return redirect(url_for('projectHeadingAdd'))
    return render_template('admin/projectHeadingAdd.html',form=form, projectheadings=projectheadings)

@app.route("/admin/projectHeadingUpdate/<id>", methods=['GET','POST'])
def projectHeadingUpdate(id):
    form=ProjectHeaderForm()
    projectheading=ProjectHeader.query.get(id)
    if request.method=='POST':
        projectheading.project_subheading=form.project_subheading.data
        projectheading.project_title=form.project_title.data
        db.session.commit()
        return redirect(url_for('projectHeadingAdd'))
    return render_template('admin/projectHeadingUpdate.html',form=form, projectheading=projectheading)

@app.route("/admin/projectHeadingDelete/<id>")
def projectHeadingDelete(id):
    projectheading=ProjectHeader.query.get(id)
    db.session.delete(projectheading)
    db.session.commit()
    return redirect(url_for('projectHeadingAdd'))
# Project Heading end



# Project Menu start
@app.route("/admin/projectmenuAdd", methods=['GET', 'POST'])
def projectmenuAdd():
    form=ProjectMenuForm()
    projectmenus=ProjectMenu.query.all()
    if request.method== "POST":
        projectmenu=ProjectMenu(
            project_menu_name=form.project_menu_name.data
        )
        db.session.add(projectmenu)
        db.session.commit()
        return redirect(url_for('projectmenuAdd'))
    return render_template('admin/projectmenuAdd.html',form=form, projectmenus=projectmenus)

@app.route("/admin/projectmenuUpdate/<id>", methods=['GET','POST'])
def projectmenuUpdate(id):
    form=ProjectMenuForm()
    projectmenu=ProjectMenu.query.get(id)
    if request.method=='POST':
        projectmenu.project_menu_name=form.project_menu_name.data
        db.session.commit()
        return redirect(url_for('projectmenuAdd'))
    return render_template('admin/projectmenuUpdate.html',form=form, projectmenu=projectmenu)

@app.route("/admin/projectmenuDelete/<id>")
def projectmenuDelete(id):
    projectmenu=ProjectMenu.query.get(id)
    db.session.delete(projectmenu)
    db.session.commit()
    return redirect(url_for('projectmenuAdd'))
# Project Menu end



# Project Box start
@app.route("/admin/projectboxAdd", methods=['GET', 'POST'])
def projectboxAdd():
    form=ProjectBoxForm()
    projectboxs=ProjectBox.query.all()
    if request.method== "POST":
        file=form.project_img.data
        project_img_name=file.filename
        randomproject=random.randint(1679,5001)
        project_name= secure_filename(form.project_name.data)
        project_extention=project_img_name.split(".")[-1]
        ProjectImg=project_name+ str(randomproject)+"."+project_extention
        file.save(os.path.join(app.config['UPLOAD_FOLDER'],ProjectImg))
        projectbox=ProjectBox(
            project_name=form.project_name.data,
            project_info=form.project_info.data,
            project_link=form.project_link.data,
            project_link_icon=form.project_link_icon.data,
            project_img=ProjectImg
        )
        db.session.add(projectbox)
        db.session.commit()
        return redirect(url_for('projectboxAdd'))
    return render_template('admin/projectboxAdd.html',form=form, projectboxs=projectboxs)

@app.route("/admin/projectboxUpdate/<id>", methods=['GET','POST'])
def projectboxUpdate(id):
    form=ProjectBoxForm()
    projectbox=ProjectBox.query.get(id)
    if request.method=='POST':
        file=form.project_img.data
        project_img_name=file.filename
        randomproject=random.randint(1679,5001)
        project_name= secure_filename(form.project_name.data)
        project_extention=project_img_name.split(".")[-1]
        ProjectImg=project_name+ str(randomproject)+"."+project_extention
        file.save(os.path.join(app.config['UPLOAD_FOLDER'],ProjectImg))
        projectbox.project_name=form.project_name.data
        projectbox.project_info=form.project_info.data
        projectbox.project_link=form.project_link.data
        projectbox.project_link_icon=form.project_link_icon.data
        projectbox.project_img=ProjectImg
        db.session.commit()
        return redirect(url_for('projectboxAdd'))
    return render_template('admin/projectboxUpdate.html',form=form, projectbox=projectbox)

@app.route("/admin/projectboxDelete/<id>")
def projectboxDelete(id):
    projectbox=ProjectBox.query.get(id)
    db.session.delete(projectbox)
    db.session.commit()
    return redirect(url_for('projectboxAdd'))
# Project Box end


# Project Button start
@app.route("/admin/projectBtnAdd", methods=['GET', 'POST'])
def projectBtnAdd():
    form=ProjectButtonForm()
    projectbtns=ProjectButton.query.all()
    if request.method== "POST":
        projectbtn=ProjectButton(
            projectbtn_title=form.projectbtn_title.data,
            projectbtn_icon=form.projectbtn_icon.data,
            projectbtn_url=form.projectbtn_url.data
        )
        db.session.add(projectbtn)
        db.session.commit()
        return redirect(url_for('projectBtnAdd'))
    return render_template('admin/projectBtnAdd.html',form=form, projectbtns=projectbtns)

@app.route("/admin/projectBtnUpdate/<id>", methods=['GET','POST'])
def projectBtnUpdate(id):
    form=ProjectButtonForm()
    projectbtn=ProjectButton.query.get(id)
    if request.method=='POST':
        projectbtn.projectbtn_title=form.projectbtn_title.data
        projectbtn.projectbtn_icon=form.projectbtn_icon.data
        projectbtn.projectbtn_url=form.projectbtn_url.data
        db.session.commit()
        return redirect(url_for('projectBtnAdd'))
    return render_template('admin/projectBtnUpdate.html',form=form, projectbtn=projectbtn)

@app.route("/admin/projectBtnDelete/<id>")
def projectBtnDelete(id):
    projectbtn=ProjectButton.query.get(id)
    db.session.delete(projectbtn)
    db.session.commit()
    return redirect(url_for('projectBtnAdd'))
# Project Button end


# Team Heading start
@app.route("/admin/teamHeadingAdd", methods=['GET', 'POST'])
def teamHeadingAdd():
    form=TeamHeadingForm()
    teamheadings=TeamHeading.query.all()
    if request.method== "POST":
        teamheading=TeamHeading(
            team_subheading=form.team_subheading.data,
            team_title=form.team_title.data
        )
        db.session.add(teamheading)
        db.session.commit()
        return redirect(url_for('teamHeadingAdd'))
    return render_template('admin/teamHeadingAdd.html',form=form, teamheadings=teamheadings)

@app.route("/admin/teamHeadingUpdate/<id>", methods=['GET','POST'])
def teamHeadingUpdate(id):
    form=TeamHeadingForm()
    teamheading=TeamHeading.query.get(id)
    if request.method=='POST':
        teamheading.team_subheading=form.team_subheading.data
        teamheading.team_title=form.team_title.data
        db.session.commit()
        return redirect(url_for('teamHeadingAdd'))
    return render_template('admin/teamHeadingUpdate.html',form=form, teamheading=teamheading)

@app.route("/admin/teamHeadingDelete/<id>")
def teamHeadingDelete(id):
    teamheading=TeamHeading.query.get(id)
    db.session.delete(teamheading)
    db.session.commit()
    return redirect(url_for('teamHeadingAdd'))
# Team Heading end



# Teammate Image Start
@app.route("/admin/teamboxAdd/", methods=['GET','POST'])
def teamboxAdd():
    form=TeamBoxForm()
    teamboxs=TeamBox.query.all()
    if request.method=='POST':
        file=form.teammate_img.data
        teammate_img_name=file.filename
        randomteammate_img=random.randint(5002,9958)
        teammate_name= secure_filename(form.teammate_name.data)
        teammate_extention=teammate_img_name.split(".")[-1]
        TeammateImg=teammate_name+ str(randomteammate_img)+"."+teammate_extention
        file.save(os.path.join(app.config['UPLOAD_FOLDER'],TeammateImg))
        teambox=TeamBox(
            teammate_name=form.teammate_name.data,
            teammate_position=form.teammate_position.data,
            teammate_img=TeammateImg
        )
        db.session.add(teambox)
        db.session.commit()
        return redirect(url_for('teamboxAdd'))
    return render_template("admin/teamboxAdd.html",form=form, teamboxs=teamboxs)

@app.route("/admin/teamboxUpdate/<id>",methods=['GET','POST'])
def teamboxUpdate(id):
    form=TeamBoxForm()
    teambox=TeamBox.query.get(id)
    if request.method=='POST':
        file=form.teammate_img.data
        teammate_img_name=file.filename
        randomteammate_img=random.randint(5002,9958)
        teammate_name= secure_filename(form.teammate_name.data)
        teammate_extention=teammate_img_name.split(".")[-1]
        TeammateImg=teammate_name+ str(randomteammate_img)+"."+teammate_extention
        file.save(os.path.join(app.config['UPLOAD_FOLDER'],TeammateImg))
        teambox.teammate_name=form.teammate_name.data
        teambox.teammate_position=form.teammate_position.data
        teambox.teammate_img=TeammateImg
        db.session.commit()
        return redirect(url_for('teamboxAdd'))
    return render_template('admin/teamboxUpdate.html',form=form, teambox=teambox)

@app.route("/admin/teamboxDelete/<id>")
def teamboxDelete(id):
    teambox=TeamBox.query.get(id)
    db.session.delete(teambox)
    db.session.commit()
    return redirect(url_for('teamboxAdd'))
# Teammate Image End



# Team Social Icon start
@app.route("/admin/teamSocilaIconAdd", methods=['GET', 'POST'])
def teamSocilaIconAdd():
    form=TeamSocilIconForm()
    teamsocialicons=TeamSocilIcon.query.all()
    if request.method== "POST":
        teamsocialicon=TeamSocilIcon(
            teammate_icon_name=form.teammate_icon_name.data,
            teammate_icon_class=form.teammate_icon_class.data,
            teammate_icon_link=form.teammate_icon_link.data
        )
        db.session.add(teamsocialicon)
        db.session.commit()
        return redirect(url_for('teamSocilaIconAdd'))
    return render_template('admin/teamSocilaIconAdd.html',form=form, teamsocialicons=teamsocialicons)

@app.route("/admin/teamSocilaIconUpdate/<id>", methods=['GET','POST'])
def teamSocilaIconUpdate(id):
    form=TeamSocilIconForm()
    teamsocialicon=TeamSocilIcon.query.get(id)
    if request.method=='POST':
        teamsocialicon.teammate_icon_name=form.teammate_icon_name.data
        teamsocialicon.teammate_icon_class=form.teammate_icon_class.data
        teamsocialicon.teammate_icon_link=form.teammate_icon_link.data
        db.session.commit()
        return redirect(url_for('teamSocilaIconAdd'))
    return render_template('admin/teamSocilaIconUpdate.html',form=form, teamsocialicon=teamsocialicon)

@app.route("/admin/teamSocilaIconDelete/<id>")
def teamSocilaIconDelete(id):
    teamsocialicon=TeamSocilIcon.query.get(id)
    db.session.delete(teamsocialicon)
    db.session.commit()
    return redirect(url_for('teamSocilaIconAdd'))
#Team Social Icon end



# Team Button start
@app.route("/admin/teambuttonAdd", methods=['GET', 'POST'])
def teambuttonAdd():
    form=TeamButtonForm()
    teambuttons=TeamButton.query.all()
    if request.method== "POST":
        teambutton=TeamButton(
            teambuuton_title=form.teambuuton_title.data,
            teambuuton_icon=form.teambuuton_icon.data,
            teambuuton_url=form.teambuuton_url.data
        )
        db.session.add(teambutton)
        db.session.commit()
        return redirect(url_for('teambuttonAdd'))
    return render_template('admin/teambuttonAdd.html',form=form, teambuttons=teambuttons)

@app.route("/admin/teambuttonUpdate/<id>", methods=['GET','POST'])
def teambuttonUpdate(id):
    form=TeamButtonForm()
    teambutton=TeamButton.query.get(id)
    if request.method=='POST':
        teambutton.teambuuton_title=form.teambuuton_title.data
        teambutton.teambuuton_icon=form.teambuuton_icon.data
        teambutton.teambuuton_url=form.teambuuton_url.data
        db.session.commit()
        return redirect(url_for('teambuttonAdd'))
    return render_template('admin/teambuttonUpdate.html',form=form, teambutton=teambutton)

@app.route("/admin/teambuttonDelete/<id>")
def teambuttonDelete(id):
    teambutton=TeamButton.query.get(id)
    db.session.delete(teambutton)
    db.session.commit()
    return redirect(url_for('teambuttonAdd'))
# Team Button end


# Client Heading start
@app.route("/admin/clientheadingAdd", methods=['GET', 'POST'])
def clientheadingAdd():
    form=ClientHeadingForm()
    clientheadings=ClientHeading.query.all()
    if request.method== "POST":
        clientheading=ClientHeading(
            client_subheading=form.client_subheading.data,
            client_title=form.client_title.data
        )
        db.session.add(clientheading)
        db.session.commit()
        return redirect(url_for('clientheadingAdd'))
    return render_template('admin/clientheadingAdd.html',form=form, clientheadings=clientheadings)

@app.route("/admin/clientheadingUpdate/<id>", methods=['GET','POST'])
def clientheadingUpdate(id):
    form=ClientHeadingForm()
    clientheading=ClientHeading.query.get(id)
    if request.method=='POST':
        clientheading.client_subheading=form.client_subheading.data
        clientheading.client_title=form.client_title.data
        db.session.commit()
        return redirect(url_for('clientheadingAdd'))
    return render_template('admin/clientheadingUpdate.html',form=form, clientheading=clientheading)

@app.route("/admin/clientheadingDelete/<id>")
def clientheadingDelete(id):
    clientheading=ClientHeading.query.get(id)
    db.session.delete(clientheading)
    db.session.commit()
    return redirect(url_for('clientheadingAdd'))
# Client Heading end




# Client Button start
@app.route("/admin/clientbuttonAdd", methods=['GET', 'POST'])
def clientbuttonAdd():
    form=ClientButtonForm()
    clientbuttons=ClientButton.query.all()
    if request.method== "POST":
        clientbutton=ClientButton(
            clientbutton_title=form.clientbutton_title.data,
            clientbutton_icon=form.clientbutton_icon.data,
            clientbutton_url=form.clientbutton_url.data
        )
        db.session.add(clientbutton)
        db.session.commit()
        return redirect(url_for('clientbuttonAdd'))
    return render_template('admin/clientbuttonAdd.html',form=form, clientbuttons=clientbuttons)

@app.route("/admin/clientbuttonUpdate/<id>", methods=['GET','POST'])
def clientbuttonUpdate(id):
    form=ClientButtonForm()
    clientbutton=ClientButton.query.get(id)
    if request.method=='POST':
        clientbutton.clientbutton_title=form.clientbutton_title.data
        clientbutton.clientbutton_icon=form.clientbutton_icon.data
        clientbutton.clientbutton_url=form.clientbutton_url.data
        db.session.commit()
        return redirect(url_for('clientbuttonAdd'))
    return render_template('admin/clientbuttonUpdate.html',form=form, clientbutton=clientbutton)

@app.route("/admin/clientbuttonDelete/<id>")
def clientbuttonDelete(id):
    clientbutton=ClientButton.query.get(id)
    db.session.delete(clientbutton)
    db.session.commit()
    return redirect(url_for('clientbuttonAdd'))
# Client Button end


# News Heading start
@app.route("/admin/newsheadingAdd", methods=['GET', 'POST'])
def newsheadingAdd():
    form=NewsHeadingForm()
    newsheadings=NewsHeading.query.all()
    if request.method== "POST":
        newsheading=NewsHeading(
            news_subheading=form.news_subheading.data,
            news_title=form.news_title.data
        )
        db.session.add(newsheading)
        db.session.commit()
        return redirect(url_for('newsheadingAdd'))
    return render_template('admin/newsheadingAdd.html',form=form, newsheadings=newsheadings)

@app.route("/admin/newsheadingUpdate/<id>", methods=['GET','POST'])
def newsheadingUpdate(id):
    form=NewsHeadingForm()
    newsheading=NewsHeading.query.get(id)
    if request.method=='POST':
        newsheading.news_subheading=form.news_subheading.data
        newsheading.news_title=form.news_title.data
        db.session.commit()
        return redirect(url_for('newsheadingAdd'))
    return render_template('admin/newsheadingUpdate.html',form=form, newsheading=newsheading)

@app.route("/admin/newsheadingDelete/<id>")
def newsheadingDelete(id):
    newsheading=NewsHeading.query.get(id)
    db.session.delete(newsheading)
    db.session.commit()
    return redirect(url_for('newsheadingAdd'))
# News Heading end



# News Box  Start
@app.route("/admin/newsboxAdd/", methods=['GET','POST'])
def newsboxAdd():
    form=NewsBoxForm()
    newsboxs=NewsBox.query.all()
    if request.method=='POST':
        file=form.newsbox_img.data
        newsbox_img_name=file.filename
        randomnewsbox_img=random.randint(12810,20006)
        newsbox_title= secure_filename(form.newsbox_title.data)
        client_extention=newsbox_img_name.split(".")[-1]
        NewsImg=newsbox_title+ str(randomnewsbox_img)+"."+client_extention
        file.save(os.path.join(app.config['UPLOAD_FOLDER'],NewsImg))
        newsbox=NewsBox(
            newsbox_title=form.newsbox_title.data,
            newsbox_desc=form.newsbox_desc.data,
            newsbox_link=form.newsbox_link.data,
            newsbox_date=form.newsbox_date.data,
            newsbox_img=NewsImg
        )
        db.session.add(newsbox)
        db.session.commit()
        return redirect(url_for('newsboxAdd'))
    return render_template("admin/newsboxAdd.html",form=form, newsboxs=newsboxs)

@app.route("/admin/newsboxUpdate/<id>",methods=['GET','POST'])
def newsboxUpdate(id):
    form=NewsBoxForm()
    newsbox=NewsBox.query.get(id)
    if request.method=='POST':
        file=form.newsbox_img.data
        newsbox_img_name=file.filename
        randomnewsbox_img=random.randint(12810,20006)
        newsbox_title= secure_filename(form.newsbox_title.data)
        client_extention=newsbox_img_name.split(".")[-1]
        NewsImg=newsbox_title+ str(randomnewsbox_img)+"."+client_extention
        file.save(os.path.join(app.config['UPLOAD_FOLDER'],NewsImg))
        newsbox.newsbox_title=form.newsbox_title.data
        newsbox.newsbox_desc=form.newsbox_desc.data
        newsbox.newsbox_link=form.newsbox_link.data
        newsbox.newsbox_date=form.newsbox_date.data
        newsbox.newsbox_img=NewsImg
        db.session.commit()
        return redirect(url_for('newsboxAdd'))
    return render_template('admin/newsboxUpdate.html',form=form, newsbox=newsbox)

@app.route("/admin/newsboxDelete/<id>")
def newsboxDelete(id):
    newsbox=NewsBox.query.get(id)
    db.session.delete(newsbox)
    db.session.commit()
    return redirect(url_for('newsboxAdd'))
# News Box End



# News Button start
@app.route("/admin/newsbuttonAdd", methods=['GET', 'POST'])
def newsbuttonAdd():
    form=NewsButtonForm()
    newsbuttons=NewsButton.query.all()
    if request.method== "POST":
        newsbutton=NewsButton(
            newsbutton_title=form.newsbutton_title.data,
            newsbutton_icon=form.newsbutton_icon.data,
            newsbutton_url=form.newsbutton_url.data
        )
        db.session.add(newsbutton)
        db.session.commit()
        return redirect(url_for('newsbuttonAdd'))
    return render_template('admin/newsbuttonAdd.html',form=form, newsbuttons=newsbuttons)

@app.route("/admin/newsbuttonUpdate/<id>", methods=['GET','POST'])
def newsbuttonUpdate(id):
    form=NewsButtonForm()
    newsbutton=NewsButton.query.get(id)
    if request.method=='POST':
        newsbutton.newsbutton_title=form.newsbutton_title.data
        newsbutton.newsbutton_icon=form.newsbutton_icon.data
        newsbutton.newsbutton_url=form.newsbutton_url.data
        db.session.commit()
        return redirect(url_for('newsbuttonAdd'))
    return render_template('admin/newsbuttonUpdate.html',form=form, newsbutton=newsbutton)

@app.route("/admin/newsbuttonDelete/<id>")
def newsbuttonDelete(id):
    newsbutton=NewsButton.query.get(id)
    db.session.delete(newsbutton)
    db.session.commit()
    return redirect(url_for('newsbuttonAdd'))
# News Button end


# Footer Info start
@app.route("/admin/footerinfoAdd", methods=['GET', 'POST'])
def footerinfoAdd():
    form=FooterCompanyInfoForm()
    company_info_footers=FooterCompanyInfo.query.all()
    if request.method== "POST":
        company_info_footer=FooterCompanyInfo(
            company_info=form.company_info.data
        )
        db.session.add(company_info_footer)
        db.session.commit()
        return redirect(url_for('footerinfoAdd'))
    return render_template('admin/footerinfoAdd.html',form=form, company_info_footers=company_info_footers)

@app.route("/admin/footerinfoUpdate/<id>", methods=['GET','POST'])
def footerinfoUpdate(id):
    form=FooterCompanyInfoForm()
    company_info_footer=FooterCompanyInfo.query.get(id)
    if request.method=='POST':
        company_info_footer.company_info=form.company_info.data
        db.session.commit()
        return redirect(url_for('footerinfoAdd'))
    return render_template('admin/footerinfoUpdate.html',form=form, company_info_footer=company_info_footer)

@app.route("/admin/footerinfoDelete/<id>")
def footerinfoDelete(id):
    company_info_footer=FooterCompanyInfo.query.get(id)
    db.session.delete(company_info_footer)
    db.session.commit()
    return redirect(url_for('footerinfoAdd'))
# Footer Info end


# Footer Social icon start
@app.route("/admin/footersocialiconAdd/", methods=['GET','POST'])
def footersocialiconAdd():
    form=FooterSocialIconForm()
    footer_social_icons=FooterSocialIcon.query.all()
    if request.method=='POST':
        footer_social_icon=FooterSocialIcon(
            footer_si_name=form.footer_si_name.data,
            footer_si_class=form.footer_si_class.data,
            footer_si_link=form.footer_si_link.data
        )
        db.session.add(footer_social_icon)
        db.session.commit()
        return redirect(url_for('footersocialiconAdd'))
    return render_template("admin/footersocialiconAdd.html",form=form, footer_social_icons=footer_social_icons)

@app.route("/admin/footersocialiconUpdate/<id>",methods=['GET','POST'])
def footersocialiconUpdate(id):
    form=FooterSocialIconForm()
    footer_social_icon=FooterSocialIcon.query.get(id)
    if request.method=='POST':
        footer_social_icon.footer_si_name=form.footer_si_name.data
        footer_social_icon.footer_si_class=form.footer_si_class.data
        footer_social_icon.footer_si_link=form.footer_si_link.data
        db.session.commit()
        return redirect(url_for('footersocialiconAdd'))
    return render_template('admin/footersocialiconUpdate.html',form=form, footer_social_icon=footer_social_icon)

@app.route("/admin/footersocialiconDelete/<id>")
def footersocialiconDelete(id):
    footer_social_icon=FooterSocialIcon.query.get(id)
    db.session.delete(footer_social_icon)
    db.session.commit()
    return redirect(url_for('footersocialiconAdd'))
# Footer Socila icon End


# Footer Meniu Name start
@app.route("/admin/footermenuAdd", methods=['GET','POST'])
def footermenuAdd():
    form=FooterMenuForm()
    footer_menus=FooterMenu.query.all()
    if request.method=='POST':
        footer_menu=FooterMenu(
            ft_menu_name=form.ft_menu_name.data,
            ft_menu_link=form.ft_menu_link.data
        )
        db.session.add(footer_menu)
        db.session.commit()
        return redirect(url_for('footermenuAdd'))
    return render_template("admin/footermenuAdd.html",form=form, footer_menus=footer_menus)

@app.route("/admin/footermenuUpdate/<id>",methods=['GET','POST'])
def footermenuUpdate(id):
    form=FooterMenuForm()
    footer_menu=FooterMenu.query.get(id)
    if request.method=='POST':
        footer_menu.ft_menu_name=form.ft_menu_name.data
        footer_menu.ft_menu_link=form.ft_menu_link.data
        db.session.commit()
        return redirect(url_for('footermenuAdd'))
    return render_template('admin/footermenuUpdate.html',form=form, footer_menu=footer_menu)

@app.route("/admin/footermenuDelete/<id>")
def footermenuDelete(id):
    footer_menu=FooterMenu.query.get(id)
    db.session.delete(footer_menu)
    db.session.commit()
    return redirect(url_for('footermenuAdd'))
# Footer Meniu Name end



# Footer Offer Name start
@app.route("/admin/footerofferAdd", methods=['GET','POST'])
def footerofferAdd():
    form=FooterOfferForm()
    footer_offers=FooterOffer.query.all()
    if request.method=='POST':
        footer_offer=FooterOffer(
            offer=form.offer.data,
            offer_link=form.offer_link.data
        )
        db.session.add(footer_offer)
        db.session.commit()
        return redirect(url_for('footerofferAdd'))
    return render_template("admin/footerofferAdd.html",form=form, footer_offers=footer_offers)

@app.route("/admin/footerofferUpdate/<id>",methods=['GET','POST'])
def footerofferUpdate(id):
    form=FooterOfferForm()
    footer_offer=FooterOffer.query.get(id)
    if request.method=='POST':
        footer_offer.offer=form.offer.data
        footer_offer.offer_link=form.offer_link.data
        db.session.commit()
        return redirect(url_for('footerofferAdd'))
    return render_template('admin/footerofferUpdate.html',form=form, footer_offer=footer_offer)

@app.route("/admin/footerofferDelete/<id>")
def footerofferDelete(id):
    footer_offer=FooterOffer.query.get(id)
    db.session.delete(footer_offer)
    db.session.commit()
    return redirect(url_for('footerofferAdd'))
# Footer Offer Name end



# Footer Social icon start
@app.route("/admin/footercontactAdd/", methods=['GET','POST'])
def footercontactAdd():
    form=FooterContactForm()
    footer_contacts=FooterContact.query.all()
    if request.method=='POST':
        footer_contact=FooterContact(
            footer_contact_name=form.footer_contact_name.data,
            footer_contact_icon=form.footer_contact_icon.data,
            footer_contact_link=form.footer_contact_link.data
        )
        db.session.add(footer_contact)
        db.session.commit()
        return redirect(url_for('footercontactAdd'))
    return render_template("admin/footercontactAdd.html",form=form, footer_contacts=footer_contacts)

@app.route("/admin/footercontactUpdate/<id>",methods=['GET','POST'])
def footercontactUpdate(id):
    form=FooterContactForm()
    footer_contact=FooterContact.query.get(id)
    if request.method=='POST':
        footer_contact.footer_contact_name=form.footer_contact_name.data
        footer_contact.footer_contact_icon=form.footer_contact_icon.data
        footer_contact.footer_contact_link=form.footer_contact_link.data
        db.session.commit()
        return redirect(url_for('footercontactAdd'))
    return render_template('admin/footercontactUpdate.html',form=form, footer_contact=footer_contact)

@app.route("/admin/footercontactDelete/<id>")
def footercontactDelete(id):
    footer_contact=FooterContact.query.get(id)
    db.session.delete(footer_contact)
    db.session.commit()
    return redirect(url_for('footercontactAdd'))
# Footer Socila icon End


# Contact Heading start
@app.route("/admin/contactheadingAdd", methods=['GET', 'POST'])
def contactheadingAdd():
    form=ContactHeadingForm()
    contactheadings=ContactHeading.query.all()
    if request.method=="POST":
        contactheading=ContactHeading(
            contact_subheding=form.contact_subheding.data,
            contact_heading=form.contact_heading.data
        )
        db.session.add(contactheading)
        db.session.commit()
        return redirect(url_for('contactheadingAdd'))
    return render_template('admin/contactheadingAdd.html',form=form, contactheadings=contactheadings)

@app.route("/admin/contactheadingUpdate/<id>", methods=['GET','POST'])
def contactheadingUpdate(id):
    form=ContactHeadingForm()
    contactheading=ContactHeading.query.get(id)
    if request.method=='POST':
        contactheading.contact_subheding=form.contact_subheding.data
        contactheading.contact_heading=form.contact_heading.data
        db.session.commit()
        return redirect(url_for('contactheadingAdd'))
    return render_template('admin/contactheadingUpdate.html',form=form, contactheading=contactheading)

@app.route("/admin/contactheadingDelete/<id>")
def contactheadingDelete(id):
    contactheading=ContactHeading.query.get(id)
    db.session.delete(contactheading)
    db.session.commit()
    return redirect(url_for('contactheadingAdd'))
# Contact Heading end



# Contact Loaction Link start
@app.route("/admin/contactmapAdd", methods=['GET', 'POST'])
def contactmapAdd():
    form=ContactMapForm()
    contactmaps=ContactMap.query.all()
    if request.method== "POST":
        contactmap=ContactMap(
            map_link=form.map_link.data
        )
        db.session.add(contactmap)
        db.session.commit()
        return redirect(url_for('contactmapAdd'))
    return render_template('admin/contactmapAdd.html',form=form, contactmaps=contactmaps)

@app.route("/admin/contactmapUpdate/<id>", methods=['GET','POST'])
def contactmapUpdate(id):
    form=ContactMapForm()
    contactmap=ContactMap.query.get(id)
    if request.method=='POST':
        contactmap.map_link=form.map_link.data
        db.session.commit()
        return redirect(url_for('contactmapAdd'))
    return render_template('admin/contactmapUpdate.html',form=form, contactmap=contactmap)

@app.route("/admin/contactmapDelete/<id>")
def contactmapDelete(id):
    contactmap=ContactMap.query.get(id)
    db.session.delete(contactmap)
    db.session.commit()
    return redirect(url_for('contactmapAdd'))
# Contact Loaction Link end



# Gallery Box  Start
@app.route("/admin/galleryboxAdd/", methods=['GET','POST'])
def galleryboxAdd():
    form=GalleryBoxForm()
    galleryboxs=GalleryBox.query.all()
    if request.method=='POST':
        file=form.gallerybox_img.data
        gallerybox_img_name=file.filename
        randomgallerybox_img=random.randint(20007,30000)
        gallerybox_title= secure_filename(form.gallerybox_title.data)
        gallerybox_extention=gallerybox_img_name.split(".")[-1]
        GalleryImg=gallerybox_title+ str(randomgallerybox_img)+"."+gallerybox_extention
        file.save(os.path.join(app.config['UPLOAD_FOLDER'],GalleryImg))
        gallerybox=GalleryBox(
            gallerybox_title=form.gallerybox_title.data,
            gallerybox_img=GalleryImg
        )
        db.session.add(gallerybox)
        db.session.commit()
        return redirect(url_for('galleryboxAdd'))
    return render_template("admin/galleryboxAdd.html",form=form, galleryboxs=galleryboxs)

@app.route("/admin/galleryboxUpdate/<id>",methods=['GET','POST'])
def galleryboxUpdate(id):
    form=GalleryBoxForm()
    gallerybox=GalleryBox.query.get(id)
    if request.method=='POST':
        file=form.gallerybox_img.data
        gallerybox_img_name=file.filename
        randomgallerybox_img=random.randint(20007,30000)
        gallerybox_title= secure_filename(form.gallerybox_title.data)
        gallerybox_extention=gallerybox_img_name.split(".")[-1]
        GalleryImg=gallerybox_title+ str(randomgallerybox_img)+"."+gallerybox_extention
        file.save(os.path.join(app.config['UPLOAD_FOLDER'],GalleryImg))
        gallerybox.gallerybox_title=form.gallerybox_title.data
        gallerybox.gallerybox_img=GalleryImg
        db.session.commit()
        return redirect(url_for('galleryboxAdd'))
    return render_template('admin/galleryboxUpdate.html',form=form, gallerybox=gallerybox)

@app.route("/admin/galleryboxDelete/<id>")
def galleryboxDelete(id):
    gallerybox=GalleryBox.query.get(id)
    db.session.delete(gallerybox)
    db.session.commit()
    return redirect(url_for('galleryboxAdd'))
# Gallery Box End


# Gallery Heading start
@app.route("/admin/galleryheadingAdd", methods=['GET', 'POST'])
def galleryheadingAdd():
    form=GalleryHeadingForm()
    galleryheadings=GalleryHeading.query.all()
    if request.method=="POST":
        galleryheading=GalleryHeading(
            gallery_subheding=form.gallery_subheding.data,
            gallery_heading=form.gallery_heading.data
        )
        db.session.add(galleryheading)
        db.session.commit()
        return redirect(url_for('galleryheadingAdd'))
    return render_template('admin/galleryheadingAdd.html',form=form, galleryheadings=galleryheadings)

@app.route("/admin/galleryheadingUpdate/<id>", methods=['GET','POST'])
def galleryheadingUpdate(id):
    form=GalleryHeadingForm()
    galleryheading=GalleryHeading.query.get(id)
    if request.method=='POST':
        galleryheading.gallery_subheding=form.gallery_subheding.data
        galleryheading.gallery_heading=form.gallery_heading.data
        db.session.commit()
        return redirect(url_for('galleryheadingAdd'))
    return render_template('admin/galleryheadingUpdate.html',form=form, galleryheading=galleryheading)

@app.route("/admin/galleryheadingDelete/<id>")
def galleryheadingDelete(id):
    galleryheading=GalleryHeading.query.get(id)
    db.session.delete(galleryheading)
    db.session.commit()
    return redirect(url_for('galleryheadingAdd'))
# gallery Heading end


# Gallery Menu start
@app.route("/admin/gallerymenuAdd", methods=['GET', 'POST'])
def gallerymenuAdd():
    form=GalleryMenuForm()
    gallerymenus=GalleryMenu.query.all()
    if request.method== "POST":
        gallerymenu=GalleryMenu(
            gallery_menu=form.gallery_menu.data
        )
        db.session.add(gallerymenu)
        db.session.commit()
        return redirect(url_for('gallerymenuAdd'))
    return render_template('admin/gallerymenuAdd.html',form=form, gallerymenus=gallerymenus)

@app.route("/admin/gallerymenuUpdate/<id>", methods=['GET','POST'])
def gallerymenuUpdate(id):
    form=GalleryMenuForm()
    gallerymenu=GalleryMenu.query.get(id)
    if request.method=='POST':
        gallerymenu.gallery_menu=form.gallery_menu.data
        db.session.commit()
        return redirect(url_for('gallerymenuAdd'))
    return render_template('admin/gallerymenuUpdate.html',form=form, gallerymenu=gallerymenu)

@app.route("/admin/gallerymenuDelete/<id>")
def gallerymenuDelete(id):
    gallerymenu=GalleryMenu.query.get(id)
    db.session.delete(gallerymenu)
    db.session.commit()
    return redirect(url_for('gallerymenuAdd'))
# Gallery Menu end


# Services Heading start
@app.route("/admin/servicesheadingAdd", methods=['GET', 'POST'])
def servicesheadingAdd():
    form=ServicesHeadingForm()
    servicesheadings=ServicesHeading.query.all()
    if request.method=="POST":
        servicesheading=ServicesHeading(
            servicessubheading=form.servicessubheading.data,
            service_heading=form.service_heading.data
        )
        db.session.add(servicesheading)
        db.session.commit()
        return redirect(url_for('servicesheadingAdd'))
    return render_template('admin/servicesheadingAdd.html',form=form, servicesheadings=servicesheadings)

@app.route("/admin/servicesheadingUpdate/<id>", methods=['GET','POST'])
def servicesheadingUpdate(id):
    form=ServicesHeadingForm()
    servicesheading=ServicesHeading.query.get(id)
    if request.method=='POST':
        servicesheading.servicessubheading=form.servicessubheading.data
        servicesheading.service_heading=form.service_heading.data
        db.session.commit()
        return redirect(url_for('servicesheadingAdd'))
    return render_template('admin/servicesheadingUpdate.html',form=form, servicesheading=servicesheading)

@app.route("/admin/servicesheadingDelete/<id>")
def servicesheadingDelete(id):
    servicesheading=ServicesHeading.query.get(id)
    db.session.delete(servicesheading)
    db.session.commit()
    return redirect(url_for('servicesheadingAdd'))
# Services Heading end



# Service BOx start
@app.route("/admin/servicesboxAdd", methods=['GET','POST'])
def servicesboxAdd():
    form=ServicesBoxForm()
    servicesboxs=ServicesBox.query.all()
    if request.method=='POST':
        servicesbox=ServicesBox(
            servicesbox_head=form.servicesbox_head.data,
            servicesbox_desc=form.servicesbox_desc.data,
            servicesbox_url=form.servicesbox_url.data,
            servicesbox_icon=form.servicesbox_icon.data
        )
        db.session.add(servicesbox)
        db.session.commit()
        return redirect(url_for('servicesboxAdd'))
    return render_template("admin/servicesboxAdd.html",form=form, servicesboxs=servicesboxs)

@app.route("/admin/servicesboxUpdate/<id>",methods=['GET','POST'])
def servicesboxUpdate(id):
    form=ServicesBoxForm()
    servicesbox=ServicesBox.query.get(id)
    if request.method=='POST':
        servicesbox.servicesbox_head=form.servicesbox_head.data
        servicesbox.servicesbox_desc=form.servicesbox_desc.data
        servicesbox.servicesbox_url=form.servicesbox_url.data
        servicesbox.servicesbox_icon=form.servicesbox_icon.data
        db.session.commit()
        return redirect(url_for('servicesboxAdd'))
    return render_template('admin/servicesboxUpdate.html',form=form, servicesbox=servicesbox)

@app.route("/admin/servicesboxDelete/<id>")
def servicesboxDelete(id):
    servicesbox=ServicesBox.query.get(id)
    db.session.delete(servicesbox)
    db.session.commit()
    return redirect(url_for('servicesboxAdd'))
# Service Box End



# About Heading start
@app.route("/admin/aboutheadingAdd", methods=['GET', 'POST'])
def aboutheadingAdd():
    form=AboutHeadingForm()
    aboutheadings=AboutHeading.query.all()
    if request.method== "POST":
        aboutheading=AboutHeading(
            about_subheading=form.about_subheading.data,
            about_heading=form.about_heading.data
        )
        db.session.add(aboutheading)
        db.session.commit()
        return redirect(url_for('aboutheadingAdd'))
    return render_template('admin/aboutheadingAdd.html',form=form, aboutheadings=aboutheadings)

@app.route("/admin/aboutheadingUpdate/<id>", methods=['GET','POST'])
def aboutheadingUpdate(id):
    form=AboutHeadingForm()
    aboutheading=AboutHeading.query.get(id)
    if request.method=='POST':
        aboutheading.about_subheading=form.about_subheading.data
        aboutheading.about_heading=form.about_heading.data
        db.session.commit()
        return redirect(url_for('aboutheadingAdd'))
    return render_template('admin/aboutheadingUpdate.html',form=form, aboutheading=aboutheading)

@app.route("/admin/aboutheadingDelete/<id>")
def aboutheadingDelete(id):
    aboutheading=AboutHeading.query.get(id)
    db.session.delete(aboutheading)
    db.session.commit()
    return redirect(url_for('aboutheadingAdd'))
# About Heading end



# About DEscription  Start
@app.route("/admin/aboutdescAdd/", methods=['GET','POST'])
def aboutdescAdd():
    form=AboutDescForm()
    aboutdesces=AboutDesc.query.all()
    if request.method=='POST':
        file=form.about_img.data
        about_img_name=file.filename
        randomabout_img=random.randint(3,300)
        about_i_extention=about_img_name.split(".")[-1]
        AboutImg="aboutimg"+str(randomabout_img)+"."+about_i_extention
        file.save(os.path.join(app.config['UPLOAD_FOLDER'],AboutImg))
        aboutdesc=AboutDesc(
            about_desc=form.about_desc.data,
            about_img=AboutImg
        )
        db.session.add(aboutdesc)
        db.session.commit()
        return redirect(url_for('aboutdescAdd'))
    return render_template("admin/aboutdescAdd.html",form=form, aboutdesces=aboutdesces)

@app.route("/admin/aboutdescUpdate/<id>",methods=['GET','POST'])
def aboutdescUpdate(id):
    form=AboutDescForm()
    aboutdesc=AboutDesc.query.get(id)
    if request.method=='POST':
        file=form.about_img.data
        about_img_name=file.filename
        randomabout_img=random.randint(3,300)
        about_i_extention=about_img_name.split(".")[-1]
        AboutImg="aboutimg"+str(randomabout_img)+"."+about_i_extention
        file.save(os.path.join(app.config['UPLOAD_FOLDER'],AboutImg))
        aboutdesc.about_desc=form.about_desc.data
        aboutdesc.about_img=AboutImg
        db.session.commit()
        return redirect(url_for('aboutdescAdd'))
    return render_template('admin/aboutdescUpdate.html',form=form, aboutdesc=aboutdesc)

@app.route("/admin/aboutdescDelete/<id>")
def aboutdescDelete(id):
    aboutdesc=AboutDesc.query.get(id)
    db.session.delete(aboutdesc)
    db.session.commit()
    return redirect(url_for('aboutdescAdd'))
# GAbout DEscription End



# Customer Heading start
@app.route("/admin/customerheadingAdd", methods=['GET', 'POST'])
def customerheadingAdd():
    form=CustomerHeadingForm()
    customerheadings=CustomerHeading.query.all()
    if request.method== "POST":
        customerheading=CustomerHeading(
            customer_subheding=form.customer_subheding.data,
            customer_heading=form.customer_heading.data,
            customer_desc=form.customer_desc.data
        )
        db.session.add(customerheading)
        db.session.commit()
        return redirect(url_for('customerheadingAdd'))
    return render_template('admin/customerheadingAdd.html',form=form, customerheadings=customerheadings)

@app.route("/admin/customerheadingUpdate/<id>", methods=['GET','POST'])
def customerheadingUpdate(id):
    form=CustomerHeadingForm()
    customerheading=CustomerHeading.query.get(id)
    if request.method=='POST':
        customerheading.customer_subheding=form.customer_subheding.data
        customerheading.customer_heading=form.customer_heading.data
        customerheading.customer_desc=form.customer_desc.data
        db.session.commit()
        return redirect(url_for('customerheadingAdd'))
    return render_template('admin/customerheadingUpdate.html',form=form, customerheading=customerheading)

@app.route("/admin/customerheadingDelete/<id>")
def customerheadingDelete(id):
    customerheading=CustomerHeading.query.get(id)
    db.session.delete(customerheading)
    db.session.commit()
    return redirect(url_for('customerheadingAdd'))
# Customer Heading end



# Brand Box  Start
@app.route("/admin/brandAdd/", methods=['GET','POST'])
def brandAdd():
    form=BrandForm()
    brands=Brand.query.all()
    if request.method=='POST':
        file=form.brand_img.data
        brand_img_name=file.filename
        randombrand_img=random.randint(30007,50000)
        brand_imgname= secure_filename(form.brand_imgname.data)
        brand_extention=brand_img_name.split(".")[-1]
        BrandImg=brand_imgname+ str(randombrand_img)+"."+brand_extention
        file.save(os.path.join(app.config['UPLOAD_FOLDER'],BrandImg))
        brand=Brand(
            brand_imgname=form.brand_imgname.data,
            brand_img=BrandImg
        )
        db.session.add(brand)
        db.session.commit()
        return redirect(url_for('brandAdd'))
    return render_template("admin/brandAdd.html",form=form, brands=brands)

@app.route("/admin/brandUpdate/<id>",methods=['GET','POST'])
def brandUpdate(id):
    form=BrandForm()
    brand=Brand.query.get(id)
    if request.method=='POST':
        file=form.brand_img.data
        brand_img_name=file.filename
        randombrand_img=random.randint(30007,50000)
        brand_imgname= secure_filename(form.brand_imgname.data)
        brand_extention=brand_img_name.split(".")[-1]
        BrandImg=brand_imgname+ str(randombrand_img)+"."+brand_extention
        file.save(os.path.join(app.config['UPLOAD_FOLDER'],BrandImg))
        brand.brand_imgname=form.brand_imgname.data
        brand.brand_img=BrandImg
        db.session.commit()
        return redirect(url_for('brandAdd'))
    return render_template('admin/brandUpdate.html',form=form, brand=brand)

@app.route("/admin/brandDelete/<id>")
def brandDelete(id):
    brand=Brand.query.get(id)
    db.session.delete(brand)
    db.session.commit()
    return redirect(url_for('brandAdd'))
# Brand Box End


# News Post Heading start
@app.route("/admin/newspostheadingAdd", methods=['GET', 'POST'])
def newspostheadingAdd():
    form=NewsPostHeadingForm()
    newspostheadings=NewsPostHeading.query.all()
    if request.method== "POST":
        newspostheading=NewsPostHeading(
            newspost_subheading=form.newspost_subheading.data,
            newspost_heading=form.newspost_heading.data
        )
        db.session.add(newspostheading)
        db.session.commit()
        return redirect(url_for('newspostheadingAdd'))
    return render_template('admin/newspostheadingAdd.html',form=form, newspostheadings=newspostheadings)

@app.route("/admin/newspostheadingUpdate/<id>", methods=['GET','POST'])
def newspostheadingUpdate(id):
    form=NewsPostHeadingForm()
    newspostheading=NewsPostHeading.query.get(id)
    if request.method=='POST':
        newspostheading.newspost_subheading=form.newspost_subheading.data
        newspostheading.newspost_heading=form.newspost_heading.data
        db.session.commit()
        return redirect(url_for('newspostheadingAdd'))
    return render_template('admin/newspostheadingUpdate.html',form=form, newspostheading=newspostheading)

@app.route("/admin/newspostheadingDelete/<id>")
def newspostheadingDelete(id):
    newspostheading=NewsPostHeading.query.get(id)
    db.session.delete(newspostheading)
    db.session.commit()
    return redirect(url_for('newspostheadingAdd'))
# News Post Heading end


# feedback form start
@app.route('/admin/feedback') 
def feedback():
   testimonials=Feedback.query.all()
   return render_template("admin/feedback.html",testimonials=testimonials)


@app.route("/admin/feedbackDelete/<id>")
def feedbackDelete(id):
   testimonial=Feedback.query.get(id)
   db.session.delete(testimonial)
   db.session.commit()
   return redirect(url_for('feedback'))

# feedback form end




@app.route('/admin/usercomment') 
def admincomment():
   usercomments=UserComment.query.all()
   return render_template("admin/usercomment.html",usercomments=usercomments)

@app.route("/admin/usercommentDelete/<id>")
def usercommentDelete(id):
   usercomment=UserComment.query.get(id)
   db.session.delete(usercomment)
   db.session.commit()
   return redirect('/admin/usercomment')