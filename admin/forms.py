from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,FileField,DateField
from wtforms.fields.core import DateTimeField
from wtforms.fields.html5 import DateTimeLocalField
from wtforms.fields.simple import TextAreaField
from wtforms.widgets.html5 import DateTimeLocalInput

class HeaderContactForm(FlaskForm):
    hc_content=StringField('hc_content')
    hc_icon_class=StringField('hc_icon_class')
    hc_url=StringField('hc_url')
    submit=SubmitField()

class HeaderSocialIconForm(FlaskForm):
    hsi_name=StringField('hsi_name')
    hsi_css_class=StringField('hsi_css_class')
    hsi_url=StringField('hsi_url')
    submit=SubmitField()

class MeniuLogoForm(FlaskForm):
    logo_title=StringField('logo_title')
    logo_url=StringField('logo_url')
    logo_alt=StringField('logo_alt')
    logo_img=FileField('logo_img')
    submit=SubmitField()
    
class MeniuNameForm(FlaskForm):
    meniu_title=StringField('meniu_title')
    meniu_url=StringField('meniu_url')
    meniu_icon=StringField('meniu_icon')
    submit=SubmitField()

class SliderForm(FlaskForm):
    slider_title=StringField('slider_title')
    slider_text=StringField('slider_text')
    slider_img=FileField('slider_img')
    slider_alt=StringField('slider_alt')
    submit=SubmitField()

class SliderUrlForm(FlaskForm):
    sliderurl_title=StringField('sliderurl_title')
    sliderurl_icon=StringField('sliderurl_icon')
    sliderurl_url=StringField('sliderurl_url')
    submit=SubmitField()

class ServiceTitleForm(FlaskForm):
    service_subheading=StringField('service_subheading')
    service_title=StringField('service_title')
    submit=SubmitField()

class ServiceItemForm(FlaskForm):
    servitem_title=StringField('servitem_title')
    servitem_text=StringField('servitem_text')
    servitem_url=StringField('servitem_url')
    servitem_icon=StringField('servitem_icon')
    submit=SubmitField()

class ServiceButtonForm(FlaskForm):
    servbttn_title=StringField('servbttn_title')
    servbttn_icon=StringField('servbttn_icon')
    servbttn_url=StringField('servbttn_url')
    submit=SubmitField()

class ReasonTitleForm(FlaskForm):
    reason_subheading=StringField('reason_subheading')
    reason_title=StringField('reason_title')
    submit=SubmitField()

class ReasonItemForm(FlaskForm):
    reasonitem_number=StringField('reasonitem_number')
    reasonitem_title=StringField('reasonitem_title')
    reasonitem_text=StringField('reasonitem_text')
    submit=SubmitField()


class ProjectHeaderForm(FlaskForm):
    project_subheading=StringField('project_subheading')
    project_title=StringField('project_title')
    submit=SubmitField()

class ProjectMenuForm(FlaskForm):
    project_menu_name=StringField('project_menu_name')
    submit=SubmitField()

class ProjectBoxForm(FlaskForm):
    project_name=StringField('project_name')
    project_info=StringField('project_info')
    project_link=StringField('project_link')
    project_link_icon=StringField('project_link_icon')
    project_img=FileField('project_img')
    submit=SubmitField()

class ProjectButtonForm(FlaskForm):
    projectbtn_title=StringField('projectbtn_title')
    projectbtn_icon=StringField('projectbtn_icon')
    projectbtn_url=StringField('projectbtn_url')
    submit=SubmitField()


class TeamHeadingForm(FlaskForm):
    team_subheading=StringField('team_subheading')
    team_title=StringField('team_title')
    submit=SubmitField()

class TeamBoxForm(FlaskForm):
    teammate_name=StringField('teammate_name')
    teammate_position=StringField('teammate_position')
    teammate_img=FileField('teammate_img')
    submit=SubmitField()

class TeamSocilIconForm(FlaskForm):
    teammate_icon_name=StringField('teammate_icon_name')
    teammate_icon_class=StringField('teammate_icon_class')
    teammate_icon_link=StringField('teammate_icon_link')
    submit=SubmitField()

class TeamButtonForm(FlaskForm):
    teambuuton_title=StringField('teambuuton_title')
    teambuuton_icon=StringField('teambuuton_icon')
    teambuuton_url=StringField('teambuuton_url')
    submit=SubmitField()

class ClientHeadingForm(FlaskForm):
    client_subheading=StringField('client_subheading')
    client_title=StringField('client_title')
    submit=SubmitField()


class ClientButtonForm(FlaskForm):
    clientbutton_title=StringField('clientbutton_title')
    clientbutton_icon=StringField('clientbutton_icon')
    clientbutton_url=StringField('clientbutton_url')
    submit=SubmitField()

class NewsHeadingForm(FlaskForm):
    news_subheading=StringField('news_subheading')
    news_title=StringField('news_title')
    submit=SubmitField()

class NewsBoxForm(FlaskForm):
    newsbox_title=StringField('newsbox_title')
    newsbox_desc=StringField('newsbox_desc')
    newsbox_link=StringField('newsbox_link')
    newsbox_img=FileField('newsbox_img')
    newsbox_date=StringField('newsbox_date')
    submit=SubmitField()

class NewsButtonForm(FlaskForm):
    newsbutton_title=StringField('newsbutton_title')
    newsbutton_icon=StringField('newsbutton_icon')
    newsbutton_url=StringField('newsbutton_url')
    submit=SubmitField()

class FooterCompanyInfoForm(FlaskForm):
    company_info=TextAreaField('company_info')
    submit=SubmitField()

class FooterSocialIconForm(FlaskForm):
    footer_si_name=StringField('footer_si_name')
    footer_si_class=StringField('footer_si_class')
    footer_si_link=StringField('footer_si_link')
    submit=SubmitField()

class FooterMenuForm(FlaskForm):
    ft_menu_name=StringField('ft_menu_name')
    ft_menu_link=StringField('ft_menu_link')
    submit=SubmitField()

class FooterOfferForm(FlaskForm):
    offer=StringField('offer')
    offer_link=StringField('offer_link')
    submit=SubmitField()

class FooterContactForm(FlaskForm):
    footer_contact_name=StringField('footer_contact_name')
    footer_contact_icon=StringField('footer_contact_icon')
    footer_contact_link=StringField('footer_contact_link')
    submit=SubmitField()

class ContactHeadingForm(FlaskForm):
    contact_subheding=StringField('Contact_subheding')
    contact_heading=StringField('Contact_heading')
    submit=SubmitField()

class ContactMapForm(FlaskForm):
    map_link=TextAreaField('map_link')
    submit=SubmitField()

class ContactFormForm(FlaskForm):
    username=StringField('username')
    userphone=StringField('userphone')
    useremail=StringField('useremail')
    usermessage=TextAreaField('useremail')
    submit=SubmitField()

class GalleryBoxForm(FlaskForm):
    gallerybox_title=StringField('gallerybox_title')
    gallerybox_img=FileField('gallerybox_img')
    submit=SubmitField()


class GalleryHeadingForm(FlaskForm):
    gallery_subheding=StringField('gallery_subheding')
    gallery_heading=StringField('gallery_heading')
    submit=SubmitField()

class GalleryMenuForm(FlaskForm):
    gallery_menu=StringField('gallery_menu')
    submit=SubmitField()

class GalleryBoxForm(FlaskForm):
    gallerybox_title=StringField('gallerybox_title')
    gallerybox_img=FileField('gallerybox_img')
    submit=SubmitField()

class ServicesHeadingForm(FlaskForm):
    servicessubheading=StringField('servicessubheading')
    service_heading=StringField('service_heading')
    submit=SubmitField()

class ServicesBoxForm(FlaskForm):
    servicesbox_head=StringField('servicesbox_head')
    servicesbox_desc=StringField('servicesbox_desc')
    servicesbox_url=StringField('servicesbox_url')
    servicesbox_icon=StringField('servicesbox_icon')
    submit=SubmitField()

class AboutHeadingForm(FlaskForm):
    about_subheading=StringField('about_subheading')
    about_heading=StringField('about_heading')
    about_desc=TextAreaField('about_desc')
    submit=SubmitField()

class AboutDescForm(FlaskForm):
    about_img=FileField('about_img')
    about_desc=TextAreaField('about_desc')
    submit=SubmitField()

class CustomerHeadingForm(FlaskForm):
    customer_subheding=StringField('customer_subheding')
    customer_heading=StringField('customer_heading')
    customer_desc=TextAreaField("customer_desc")
    submit=SubmitField()

class BrandForm(FlaskForm):
    brand_imgname=StringField('brand_imgname')
    brand_img=FileField('brand_img')
    submit=SubmitField()

class NewsPostHeadingForm(FlaskForm):
    newspost_subheading=StringField('newspost_subheading')
    newspost_heading=StringField('newspost_heading')
    submit=SubmitField()

class FeedbackForm(FlaskForm):
    clientname=StringField('clientname')
    clientemail=StringField('clientemail')
    clientphoto=FileField('clientphoto')
    clientmessage=TextAreaField('clientmessage')
    submit=SubmitField()






class UserCommentForm(FlaskForm):
    commentusername=StringField('commentusername')
    commentuseremail=StringField('commentuseremail')
    commentdate=DateField('commentdate')
    comment=TextAreaField('comment')
    submit=SubmitField()

"""class Form(FlaskForm):
    =StringField()
    =FileField()
    submit=SubmitField()"""