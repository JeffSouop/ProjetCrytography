from cryptography import x509
from cryptography.hazmat.backends import default_backend
import base64


cert_str = """
-----BEGIN CERTIFICATE-----
MIIITTCCBjWgAwIBAgIQLfiS9DiZiaruFvA/IweC8zANBgkqhkiG9w0BAQsFADB9
MQswCQYDVQQGEwJGUjESMBAGA1UECgwJREhJTVlPVElTMRwwGgYDVQQLDBMwMDAy
IDQ4MTQ2MzA4MTAwMDM2MR0wGwYDVQRhDBROVFJGUi00ODE0NjMwODEwMDAzNjEd
MBsGA1UEAwwUQ2VydGlnbmEgU2VydmljZXMgQ0EwHhcNMjMwNDI3MjIwMDAwWhcN
MjQwNDI2MjE1OTU5WjB9MQswCQYDVQQGEwJGUjEOMAwGA1UEBwwFUEFSSVMxNDAy
BgNVBAoMK0NBSVNTRSBOQVRJT05BTEUgREVTIEFMTE9DQVRJT05TIEZBTUlMSUFM
RVMxEzARBgNVBAMMCnd3dy5jYWYuZnIxEzARBgNVBAUTClMyNzExOTE0NzgwggEi
MA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQDcYARr1Xgw4mt557yCYUSn/Snx
7zHxwe4eXC5tFVYHquPuMaZah2Aldo/78V9msLAkOmgQ0w1W2XjmNfLLuNRqV+s1
UVliH2IRdzvLqUgvQvCCookLhONC2R0sUpMju7Dx+tcKQSh61xyRxKqDD3lPQaN+
otUfW17d5+Hf1vf7Q56a6JsegVkDZ72XCGLCe1nsFS8ofqbS3DvgAp4lSdDKRUh+
UNW6EriO11skX0lJNs0JgwAi73n7AN3kU4g6nVzR+wYJ3yj/DvVOz8sZSyL7sQdV
jlnY+hCDcjQ5Cs3XEHAggp0scXzzV1XISihCFFJS2wOFKzzzedPI8U4lRxPpAgMB
AAGjggPHMIIDwzCB5AYIKwYBBQUHAQEEgdcwgdQwNgYIKwYBBQUHMAKGKmh0dHA6
Ly9hdXRvcml0ZS5jZXJ0aWduYS5mci9zZXJ2aWNlc2NhLmRlcjA4BggrBgEFBQcw
AoYsaHR0cDovL2F1dG9yaXRlLmRoaW15b3Rpcy5jb20vc2VydmljZXNjYS5kZXIw
MAYIKwYBBQUHMAGGJGh0dHA6Ly9zZXJ2aWNlc2NhLm9jc3AuZGhpbXlvdGlzLmNv
bTAuBggrBgEFBQcwAYYiaHR0cDovL3NlcnZpY2VzY2Eub2NzcC5jZXJ0aWduYS5m
cjAfBgNVHSMEGDAWgBSs7IaPSzccuH8XGxnQruhO4zRcEjAJBgNVHRMEAjAAMGEG
A1UdIARaMFgwCAYGZ4EMAQICMEwGCyqBegGBMQIFAQEBMD0wOwYIKwYBBQUHAgEW
L2h0dHBzOi8vd3d3LmNlcnRpZ25hLmNvbS9hdXRvcml0ZS1jZXJ0aWZpY2F0aW9u
MGUGA1UdHwReMFwwK6ApoCeGJWh0dHA6Ly9jcmwuY2VydGlnbmEuZnIvc2Vydmlj
ZXNjYS5jcmwwLaAroCmGJ2h0dHA6Ly9jcmwuZGhpbXlvdGlzLmNvbS9zZXJ2aWNl
c2NhLmNybDATBgNVHSUEDDAKBggrBgEFBQcDATAOBgNVHQ8BAf8EBAMCBaAwHQYD
VR0RBBYwFIIGY2FmLmZyggp3d3cuY2FmLmZyMB0GA1UdDgQWBBSf2wwntwbVJGio
pjwC8FANsE5StDCCAX8GCisGAQQB1nkCBAIEggFvBIIBawFpAHYA7s3QZNXbGs7F
XLedtM0TojKHRny87N7DUUhZRnEftZsAAAGHyB7g7QAABAMARzBFAiBuXQNE5a91
63sJkNxOPgNrtg3SR4H0Nm5WwKd6xJy51QIhAP0eDmtPAnAVMDT9cjYjRhzrRQgE
DDXNrgnckwClvQWmAHcAdv+IPwq2+5VRwmHM9Ye6NLSkzbsp3GhCCp/mZ0xaOnQA
AAGHyB7c9QAABAMASDBGAiEAo8cOusW+YtEgkj33GZW2Aa6VmfYAgo8KOfLa9bXh
QMsCIQD0w/SmsL+fvs6JUelWpKhEY4MFZzFnun2f7DJUs7dQDAB2AFWB1MIWkDYB
SuoLm1c8U/DA5Dh4cCUIFy+jqh0HE9MMAAABh8ge5T8AAAQDAEcwRQIhANB3fujB
5XX3G85zSaGq501tAFNfugvHYonTKPE+oSHIAiAJGgCNOfCRQatTdeMoXP2YtVpI
cBTGoYNJyBOEVquAfDANBgkqhkiG9w0BAQsFAAOCAgEALRiclCwz0h+GiRh1DSHR
jsYBuI+/pHUiJKbCgihLVewGs7ZcFciYaZI6iuENMq+4Tm9UYYh4DqCfLjB4do7O
eZNLLoAlU20dvgxJkF5/NIoXiAoxWjPFloSvJnjIrRi5TsXjFYsM5Ar2j1sI9Cl0
EFD0EH9FtPkzB0eHOBNuNfYFlcm7X9YnnMKw4x9Ea2xAjdJ93GaH6oL7oSrgGttv
V2i2GFuDOptisBAT1Ki4afXl0Vlt9tOCAWHrlU90Cbd526MTOustzfbT+x5moo1E
DbBDAhj4my1ihMiDykNMwv2xXxTVjSVZJNhHUZq+0FLhbiJUQ+q8WGfSF42JIsWe
Q35oSIEornW1NgJsxq0gHmhpVfC+fFj1i0Kffj/TPGcQt5UXRpECC/5UOyg0xh0q
ArBmY+NWY1yDbalK5H47mGSlY0dHQFlj5mVvo2suqrYMr/64oHY73FtM3aOPAmVj
ABkGlaDwj+R3Xv9Udmxs0ciVtinEhCVBC2Kd452F1KjqXVCeIfIjfBMg70GxUht/
GTnBYEIhkkdglY+Yy7M6dZ4NDlWlgmA+m3XOjdm1nKN966vp1l+K6H6WJ2tz8Ewf
574iZIHXnytg+uiFnmV71yKxupUxO9yV4a7tFaXLpv8DVwkg6BEhbNSurXbiFncl
evoxTMXRUXQ9jpHcwyD/iaY=
-----END CERTIFICATE-----
"""


def extract_domain_names(cert_str):
    # Conversion du certificat en format DER pour l'analyser
    cert_der = base64.b64decode(cert_str.strip().split('\n', 1)[1].rsplit('\n', 1)[0])
    cert = x509.load_der_x509_certificate(cert_der, default_backend())

    # Extraire le Common Name
    common_name = cert.subject.get_attributes_for_oid(x509.NameOID.COMMON_NAME)[0].value
    print(f"{common_name}")

    # Vérifier et extraire les Subject Alternative Names, s'ils existent
    try:
        san = cert.extensions.get_extension_for_oid(x509.ExtensionOID.SUBJECT_ALTERNATIVE_NAME).value
        # print("Subject Alternative Names:")
        for name in san:
            pass
            # print(name)
    except x509.ExtensionNotFound:
        pass
        # print("No Subject Alternative Name extension found in the certificate.")

extract_domain_names(cert_str)