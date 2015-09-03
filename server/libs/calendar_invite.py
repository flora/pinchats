import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email.Utils import COMMASPACE, formatdate
from email import Encoders
import os,datetime
from server.libs.calendar_free import get_free_time

def send_calendar_invites(user_emails):
    CRLF = "\r\n"
    login = "anshul@pinterest.com"
    password = "<PUT PASSWORD HERE>"
    attendees = user_emails
    organizer = "ORGANIZER;CN=PinChats:mailto:pinchats"+CRLF+" @pinterest.com"
    fro = "PinChats <pinchats@pinterest.com>"
    
    ddtstart, dtend = get_free_time(user_emails)
    if not ddtstart:
         # could not find any overlapping times for the users
         return
    dtstamp = datetime.datetime.now().strftime("%Y%m%dT%H%M%SZ")
    dtstart = ddtstart.strftime("%Y%m%dT%H%M%SZ")
    dtend = dtend.strftime("%Y%m%dT%H%M%SZ")
   
    description = "DESCRIPTION: test invitation from pyICSParser"+CRLF
    attendee = ""
    for att in attendees:
        attendee += "ATTENDEE;CUTYPE=INDIVIDUAL;ROLE=REQ-    PARTICIPANT;RSVP=TRUE"+CRLF+" ;CN="+att+";X-NUM-GUESTS=0:"+CRLF+" mailto:"+att+CRLF

    ical = "BEGIN:VCALENDAR"+CRLF+"PRODID:pyICSParser"+CRLF+"VERSION:2.0"+CRLF+"CALSCALE:GREGORIAN"+CRLF
    ical+="METHOD:REQUEST"+CRLF+"BEGIN:VEVENT"+CRLF+"DTSTART:"+dtstart+CRLF+"DTEND:"+dtend+CRLF+"DTSTAMP:"+dtstamp+CRLF+organizer+CRLF
    ical+= "UID:FIXMEUID"+dtstamp+CRLF
    ical+= attendee+"CREATED:"+dtstamp+CRLF+description+"LAST-MODIFIED:"+dtstamp+CRLF+"LOCATION:"+CRLF+"SEQUENCE:0"+CRLF+"STATUS:CONFIRMED"+CRLF
    ical+= "SUMMARY:test "+ddtstart.strftime("%Y%m%d @ %H:%M")+CRLF+"TRANSP:OPAQUE"+CRLF+"END:VEVENT"+CRLF+"END:VCALENDAR"+CRLF

    eml_body = "You've got a PinChat scheduled! Feel free to coordinate and reschedule at a more convenient time. Plan to meet by the blue art structure in 808 near the 572 7th Strreet."
    eml_body_bin = "This is the email body in binary - two steps"
    msg = MIMEMultipart('mixed')
    msg['Reply-To']=fro
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = "pyICSParser invite"+dtstart
    msg['From'] = fro
    msg['To'] = ",".join(attendees)

    part_email = MIMEText(eml_body,"html")
    part_cal = MIMEText(ical,'calendar;method=REQUEST')

    msgAlternative = MIMEMultipart('alternative')
    msg.attach(msgAlternative)

    ical_atch = MIMEBase('application/ics',' ;name="%s"'%("invite.ics"))
    ical_atch.set_payload(ical)
    Encoders.encode_base64(ical_atch)
    ical_atch.add_header('Content-Disposition', 'attachment; filename="%s"'%("invite.ics"))

    eml_atch = MIMEBase('text/plain','')
    Encoders.encode_base64(eml_atch)
    eml_atch.add_header('Content-Transfer-Encoding', "")

    msgAlternative.attach(part_email)
    msgAlternative.attach(part_cal)

    mailServer = smtplib.SMTP('smtp.gmail.com', 587)
    mailServer.ehlo()
    mailServer.starttls()
    mailServer.ehlo()
    mailServer.login(login, password)
    mailServer.sendmail(fro, attendees, msg.as_string())
    mailServer.close()
