from app import db

class HeaderContact(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    hc_content=db.Column(db.String(255))
    hc_icon_class=db.Column(db.String(255))
    hc_url=db.Column(db.String(255))

class HeaderSocialIcon(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    hsi_name=db.Column(db.String(255))
    hsi_css_class=db.Column(db.String(255))
    hsi_url=db.Column(db.String(255))

class MeniuLogo(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    logo_title=db.Column(db.String(255))
    logo_url=db.Column(db.String(255))
    logo_alt=db.Column(db.String(255))
    logo_img=db.Column(db.String(255))

class MeniuName(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    meniu_title=db.Column(db.String(255))
    meniu_url=db.Column(db.String(255))
    meniu_icon=db.Column(db.String(255))

class Slider(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    slider_title=db.Column(db.String(255))
    slider_text=db.Column(db.String(255))
    slider_img=db.Column(db.String(255))
    slider_alt=db.Column(db.String(255))

class SliderUrl(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    sliderurl_title=db.Column(db.String(255))
    sliderurl_icon=db.Column(db.String(255))
    sliderurl_url=db.Column(db.String(255))

class ServiceTitle(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    service_subheading=db.Column(db.String(255))
    service_title=db.Column(db.String(255))

class ServiceItem(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    servitem_title=db.Column(db.String(255))
    servitem_text=db.Column(db.String(255))
    servitem_url=db.Column(db.String(255))
    servitem_icon=db.Column(db.String(255))

class ServiceButton(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    servbttn_title=db.Column(db.String(255))
    servbttn_icon=db.Column(db.String(255))
    servbttn_url=db.Column(db.String(255))

class ReasonTitle(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    reason_subheading=db.Column(db.String(255))
    reason_title=db.Column(db.String(255))

class ReasonItem(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    reasonitem_number=db.Column(db.String(255))
    reasonitem_title=db.Column(db.String(255))
    reasonitem_text=db.Column(db.String(255))

class ProjectHeader(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    project_subheading=db.Column(db.String(255))
    project_title=db.Column(db.String(255))

class ProjectMenu(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    project_menu_name=db.Column(db.String(255))

class ProjectBox(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    project_name=db.Column(db.String(255))
    project_info=db.Column(db.String(255))
    project_link=db.Column(db.String(255))
    project_link_icon=db.Column(db.String(255))
    project_img=db.Column(db.String(255))

class ProjectButton(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    projectbtn_title=db.Column(db.String(255))
    projectbtn_icon=db.Column(db.String(255))
    projectbtn_url=db.Column(db.String(255))

class TeamHeading(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    team_subheading=db.Column(db.String(255))
    team_title=db.Column(db.String(255))

class TeamBox(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    teammate_img=db.Column(db.String(255))
    teammate_name=db.Column(db.String(255))
    teammate_position=db.Column(db.String(255))

class TeamSocilIcon(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    teammate_icon_name=db.Column(db.String(255))
    teammate_icon_class=db.Column(db.String(255))
    teammate_icon_link=db.Column(db.String(255))

class TeamButton(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    teambuuton_title=db.Column(db.String(255))
    teambuuton_icon=db.Column(db.String(255))
    teambuuton_url=db.Column(db.String(255))

class ClientHeading(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    client_subheading=db.Column(db.String(255))
    client_title=db.Column(db.String(255))


class ClientButton(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    clientbutton_title=db.Column(db.String(255))
    clientbutton_icon=db.Column(db.String(255))
    clientbutton_url=db.Column(db.String(255))

class NewsHeading(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    news_subheading=db.Column(db.String(255))
    news_title=db.Column(db.String(255))

class NewsBox(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    newsbox_title=db.Column(db.String(255))
    newsbox_desc=db.Column(db.String(255))
    newsbox_link=db.Column(db.String(255))
    newsbox_img=db.Column(db.String(255))
    newsbox_date=db.Column(db.String(255))

class NewsButton(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    newsbutton_title=db.Column(db.String(255))
    newsbutton_icon=db.Column(db.String(255))
    newsbutton_url=db.Column(db.String(255))

class FooterCompanyInfo(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    company_info=db.Column(db.String(255))

class FooterSocialIcon(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    footer_si_name=db.Column(db.String(255))
    footer_si_class=db.Column(db.String(255))
    footer_si_link=db.Column(db.String(255))

class FooterMenu(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    ft_menu_name=db.Column(db.String(255))
    ft_menu_link=db.Column(db.String(255))

class FooterOffer(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    offer=db.Column(db.String(255))
    offer_link=db.Column(db.String(255))

class FooterContact(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    footer_contact_name=db.Column(db.String(255))
    footer_contact_icon=db.Column(db.String(255))
    footer_contact_link=db.Column(db.String(255))

class ContactHeading(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    contact_subheding=db.Column(db.String(255))
    contact_heading=db.Column(db.String(255))

class ContactMap(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    map_link=db.Column(db.String(255))

class ContactForm(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(255))
    userphone=db.Column(db.String(255))
    useremail=db.Column(db.String(255))
    usermessage=db.Column(db.Text)

class GalleryBox(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    gallerybox_title=db.Column(db.String(255))
    gallerybox_img=db.Column(db.String(255))

class GalleryHeading(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    gallery_subheding=db.Column(db.String(255))
    gallery_heading=db.Column(db.String(255))

class GalleryMenu(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    gallery_menu=db.Column(db.String(255))

class ServicesHeading(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    servicessubheading=db.Column(db.String(255))
    service_heading=db.Column(db.String(255))

class ServicesBox(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    servicesbox_head=db.Column(db.String(255))
    servicesbox_desc=db.Column(db.String(255))
    servicesbox_url=db.Column(db.String(255))
    servicesbox_icon=db.Column(db.String(255))

class AboutHeading(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    about_subheading=db.Column(db.String(255))
    about_heading=db.Column(db.String(255))

class AboutDesc(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    about_img=db.Column(db.String(255))
    about_desc=db.Column(db.Text)

class CustomerHeading(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    customer_subheding=db.Column(db.String(255))
    customer_heading=db.Column(db.String(255))
    customer_desc=db.Column(db.Text)
    
class Brand(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    brand_imgname=db.Column(db.String(255))
    brand_img=db.Column(db.String(255))

class NewsPostHeading(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    newspost_subheading=db.Column(db.String(255))
    newspost_heading=db.Column(db.String(255))

class Feedback(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    clientname=db.Column(db.String(255))
    clientemail=db.Column(db.String(255))
    clientphoto=db.Column(db.String(255))
    clientmessage=db.Column(db.Text)


class UserComment(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    commentusername=db.Column(db.String(255))
    commentuseremail=db.Column(db.String(255))
    commentdate=db.Column(db.Date)
    comment=db.Column(db.String(255))