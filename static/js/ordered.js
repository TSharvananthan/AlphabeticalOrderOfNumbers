function search() {
  let listElements = document.getElementById("list-id").getElementsByTagName("li");
  let input = document.getElementById("search-id").value;
  for (listItem of listElements) {
    if (listItem.innerHTML.includes(input)) {
      listItem.style.display = "";
    } else {
      listItem.style.display = "none";
    }
  };
};

function changeColumnCount(columnsWanted) {
  document.getElementById("list-id").style.columnCount = columnsWanted;
  return 0;
}
