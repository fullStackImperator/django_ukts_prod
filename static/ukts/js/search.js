const url = window.location.href
const searchForm = document.getElementById('search-form')
const searchInput = document.getElementById('search-input')
const resultsBox = document.getElementById('results-box')

const csrf = document.getElementsByName('csrfmiddlewaretoken')[0].value

console.log(searchInput)

const sendSearchData = (trener) => {
    $.ajax({
        type: 'POST',
        url: 'search/',
        data: {
            'csrfmiddlewaretoken': csrf,
            'trener': trener,
        },
        // success: (res) => {
        //     console.log(res.data)
        //     const data = res.data
        //     if (Array.isArray(data)) {
        //         // console.log("We have an Array")
        //         resultsBox.innerHTML = ""
        //         data.forEach(trener => {
        //             resultsBox.innerHTML += 
        //             `
        //                 <a href="${url}${trener.pk}" class="item">
        //                     <div class="row mt-2 mb-2">
        //                         <div class="col-2">
        //                             <img src="${trener.slika}" class="trener-img">
        //                         </div>
        //                         <div class="col-10">
        //                             <h5>${trener.ime}</h5>
        //                             <p class="text-muted">${trener.licenca}</p>
        //                         </div>
        //                     </div>
        //                 </a>
        //             `
        //         })
        //     }
        //     else {
        //         if (searchInput.value.length > 0) {
        //             resultsBox.innerHTML = `<b>${data}</b>`
        //         } else {
        //             resultsBox.classList.add('not-visible')
        //         }
        //     }
        // },
        success: (res) => {
            console.log(res.data)
            const data = res.data
            if (Array.isArray(data)) {
                // console.log("We have an Array")
                rezultati.innerHTML = ""
                data.forEach(trener => {
                    rezultati.innerHTML += 
                    `
                        <div class="row align-items-center py-3 border-bottom">
                        
                            <div class="col-sm-7">
                            <div class="row align-items-center">
                                <div class="col">
                                <div class="row g-0 align-items-center">
                                    <div class="col-auto"><img class="me-3" src="${trener.slika}" alt="" width="50" height="50" /></div>
                                        <div class="col-8 mt-2">
                                            <a class="text-black" href="#!">
                                                <h5 class="fw-bold mb-0">${trener.ime}</h5>
                                            </a>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            </div>
                            <div class="col-sm-5 mt-4 mt-sm-0">
                            <div class="row align-items-center justify-content-end">
                                <div class="col-3 col-sm-6 text-end text-sm-center">

                                </div>
                                <div class="col-3 col-sm-6 text-end">
                                <h6 class="fs-0 fw-normal mb-0 text-end">${trener.licenca}</h6>
                                </div>
                            </div>
                            </div>
                            
                        </div>
                        

                    `
                })
            }
            else {
                if (searchInput.value.length > 0) {
                    rezultati.innerHTML = `<b>${data}</b>`
                } else {
                    rezultati.classList.add('not-visible')
                }
            }
        },









        error: (err) => {
            console.log(err)
        },

    })
}


searchInput.addEventListener('keyup', e=>{
    console.log(e.target.value)

    if (rezultati.classList.contains('not-visible')){
        rezultati.classList.remove('not-visible')
    }

    sendSearchData(e.target.value)

})