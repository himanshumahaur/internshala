let url = "https://api.airtable.com/v0/appQsEV94eQuwURPi/tblgkvDKVKpNbWV2L";

let headers = {
    "Authorization": "Bearer patijTY4ITapmTa9W.8ca91c85013328f160b793d0ab2be245c1777f628b1450009345ab0f0fc2d2a6"
}

async function getdetails() {
  const response = await fetch(url, {
    headers: headers
  });
  
  const data = await response.json();

  data.records.forEach(record => {
      console.log(`Details: ${record.fields.FirstName} ${record.fields.LastName} ${record.fields.Status}`);
  });
}

getdetails();