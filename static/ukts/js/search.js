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
                            
                    <div class="col-sm-12">
                      <div class="row align-items-center">
                        <div class="col">

                          <div class="row g-0 align-items-center">
                            
                            <div class="col-6 mt-2">
                                <h5 class="fw-bold mb-0 alignleft">${trener.ime}</h5>
                                
                                <h5 class="fw-bold mb-0 alignleft"> &nbsp ${trener.prezime}</h5>
                            </div>
                            <div class="col-3 mt-2">
                                <h6 class="fs-0 fw-normal mb-0 text-end">${trener.licenca}</h6>
                            </div>
                            <div class="col-3 mt-2">
                                <h6 class="fs-0 fw-normal mb-0 text-end">${trener.boja}</h6>
                            </div>
                          </div>
                          

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







                        // <div class="row align-items-center py-3 border-bottom">
                        
                        //     <div class="col-7">
                        //     <div class="row align-items-center">
                        //         <div class="col">
                        //         <div class="row g-0 align-items-center">
                        //             <div class="col-auto"><img class="me-3" src="${trener.slika}" alt="" width="50" height="50" /></div>
                        //                 <div class="col-8 mt-2">
                        //                     <a class="text-black" href="#!">
                        //                         <h5 class="fw-bold mb-0">${trener.ime}</h5>
                        //                     </a>
                        //                 </div>
                        //             </div>
                        //         </div>
                        //     </div>
                        //     </div>
                        //     <div class="col-sm-5 mt-4 mt-sm-0">
                        //     <div class="row align-items-center justify-content-end">
                        //         <div class="col-3 col-sm-6 text-end text-sm-center">
                        //             <h6 class="fs-0 fw-normal mb-0 text-end">${trener.licenca}</h6>
                        //         </div>
                        //     </div>
                        //     </div>
                            
                        // </div>
                        
