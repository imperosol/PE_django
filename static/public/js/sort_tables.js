function mustBeSwaped(x, y) {
    if (isNaN(x.innerHTML) || isNaN(y.innerHTML)) {
        return x.innerHTML.toLowerCase() > y.innerHTML.toLowerCase();
    }
    return parseInt(x.innerHTML) > parseInt(y.innerHTML);
}

function removeChevrons(row) {
    let columns = row.getElementsByTagName('th');
    for (let i = 0; i < columns.length; i++) {
        columns[i].innerHTML = columns[i].innerHTML.replace("<span class=\"glyphicon glyphicon-chevron-down\"></span>", "");
    }
}

function getColumn() {
    let e = document.getElementById("sort-by-column");
    return parseInt(e.options[e.selectedIndex].value);
}

function sortTable(tableID, n) {
    if (arguments.length === 1) {
        n = getColumn();
    }
    let rows = document.getElementById(tableID).rows;
    removeChevrons(rows[0]);
    rows[0].getElementsByTagName("th")[n].innerHTML += " <span class=\"glyphicon glyphicon-chevron-down\"></span>";
    let switching = true;
    while (switching) {
        switching = false;
        for (let i = 1; i < rows.length - 1; i++) {
            let x = rows[i].getElementsByTagName("td")[n];
            let y = rows[i + 1].getElementsByTagName("td")[n];
            if (mustBeSwaped(x, y)) {
                rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
                switching = true;
                break;
            }
        }
    }
}
