function info(id,title,date,description) {
  let div = document.getElementById("infoTask")
  div.innerHTML = '<p>ID:&nbsp'+id+'</p><p>Title:&nbsp'+title+'</p><p>Date:&nbsp'+date+'</p><p>Description:&nbsp'+description+'</p>';
}

function copyToken(){
  let copyText = document.getElementById("tokenInput");
  copyText.select();
  copyText.setSelectionRange(0, 99999);
  navigator.clipboard.writeText(copyText.value);
  alert("Copied token: " + copyText.value);
}

function deleteTask(task_id){
  let p = document.getElementById("deleteMessage")
  let yesButtonDelete = document.getElementById("yesButtonDelete")
  p.innerHTML = 'Delete task&nbsp'+task_id+'&nbsp?'
  yesButtonDelete.value = task_id
}
