document.addEventListener("DOMContentLoaded", () => {
    const rows = document.querySelectorAll('tr[data-href]');

    console.log(rows)
    rows.forEach (row => {
        row.addEventListener("click", () => {
            window.location.href = row.dataset.href;
        });
    });
});
$(document).ready(function(){
    $('table tr').on('hover', function(){
        $(this).hide(300);
    })
})