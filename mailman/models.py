from django.db import models

class WebHandler(models.Model):
    url = models.URLField(unique=True)
    is_active = models.BooleanField(default=True)

    def __unicode__(self):
        return self.url

class Recipient(models.Model):
    web_handler = models.ForeignKey(WebHandler)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    linkedin_link = models.URLField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    def __unicode__(self):
        return "%s %s" % (self.first_name, self.last_name)

class MailData(models.Model):
    web_handler = models.ForeignKey(WebHandler)
    contacted_yn = models.BooleanField(default=False)
    interaction_notes = models.CharField(max_length=300, null=True, blank=True)
    website_type = models.CharField(max_length=150, null=True, blank=True)
    category = models.CharField(max_length=150, null=True, blank=True)
    segment_contact_title = models.CharField(max_length=150, null=True, blank=True)
    platform_shpcart = models.CharField(max_length=150, null=True, blank=True)
    lower_adwordsppcdaily_tspyfl = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    upper_adwordsppcdaily_tspyfl = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    avg_adpos_tspyf = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    advertisers_tspyf = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    value_organictrafficday_tspyf = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    value_paidtrafficday_tspyf = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    paidclickday_tspyf = models.CharField(max_length=10, null=True, blank=True)
    organicclickday_tspyf = models.CharField(max_length=10, null=True, blank=True)
    tea_value = models.CharField(max_length=10, null=True, blank=True)
    rmt_value = models.CharField(max_length=10, null=True, blank=True)
    name_reg_twhxa = models.CharField(max_length=150, null=True, blank=True)
    whois_url_twhxa = models.CharField(max_length=150, null=True, blank=True)
    contact_url_twhxa = models.URLField(blank=True, null=True)
    phone1_twhxa = models.CharField(max_length=50, blank=True, null=True)
    Phone2_twhxa = models.CharField(max_length=50, blank=True, null=True)
    email_twhxa = models.EmailField(blank=True, null=True)
    communication_notes = models.CharField(max_length=500, blank=True, null=True)
    scrape_source = models.CharField(max_length=150, blank=True, null=True)
    group = models.CharField(max_length=50, blank=True, null=True)
    test_domain = models.URLField(blank=True, null=True)
    low_ppcbudget_tispg = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    high_ppcbudget_tispg = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    low_lastmonthclix_tispg = models.CharField(max_length=10, blank=True, null=True)
    high_lastmonthclix_tispg = models.CharField(max_length=10, blank=True, null=True)
    avg_adpos_tispg = models.CharField(max_length=10, blank=True, null=True)
    goog_ppckeywds_tispg = models.CharField(max_length=250, blank=True, null=True)
    yahoo_ppckeywds_tispg = models.CharField(max_length=250, blank=True, null=True)
    competitor1_tispg = models.CharField(max_length=10, blank=True, null=True)
    competitor2_tispg = models.CharField(max_length=10, blank=True, null=True)
    competitor3_tispg = models.CharField(max_length=10, blank=True, null=True)
    competitor4_tispg = models.CharField(max_length=10, blank=True, null=True)
    competitor5_tispg = models.CharField(max_length=10, blank=True, null=True)

    def __unicode__(self):
        return "%s" % self.web_handler.url

    class Meta:
        verbose_name_plural = "Mail Data"



