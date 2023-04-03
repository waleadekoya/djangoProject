const url = 'https://swapi.dev/api/people';

// 1. jquery ajax method
$.ajax({
    type: 'GET',
    url: url,
    success: function (response) {console.log('jquery ajax', response)},
    error: function (error) {
        console.log(error);
    }
})

// 2. XMLHttpRequest
const req = new XMLHttpRequest()

req.addEventListener('readystatechange', ()=> {
    if (req.readyState === 4) {
        console.log('xhttp', JSON.parse(req.responseText))
    }
})

req.open('GET', url)
req.send()


// 3. FetchAPI

fetch(url)
    .then(response => response.json())
    .then(data => console.log('fetch', data))
    .catch(err => console.log(err))