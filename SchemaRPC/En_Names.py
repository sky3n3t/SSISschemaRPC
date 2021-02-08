classes={"Matematik":"Ma","Idrott":"IDH","Engelska":"En","Svenska":"Sv","Samhällskunskap":"So","Klassråd":"Klassråd","Expert":"ET","Teknik":"Te","Kemi":"Ke","break":"break"}
def en_name(s):
    try:
        out=classes.get(s)
        return(out)
    except:
        return("false")
