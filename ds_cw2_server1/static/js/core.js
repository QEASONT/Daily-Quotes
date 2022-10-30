$(document).ready(function () {
    // edit item
    $(".edit-btn").on('click', function () {

        var itemId = this.id;
        $("#item" + itemId).hide();
        $("#form" + itemId).show();
        $(".cancel-btn").click(function () {
            $("#form" + itemId).hide();
            $("#item" + itemId).show();
        });
    });
    $(".importancebtn").on('click', function () {

        var temp = document.getElementById("importantid");
        temp.value = this.id.slice(3);
        for (i = 1; i < 4; i++) {
            if (this.id == "imp" + String(i)) {
                for (j = 1; j < 4; j++) {
                    if (i == j) {

                        document.getElementById("imp" + String(i)).className = "importancebtn btn mr-1 backcolor-grey";
                    } else {
                        document.getElementById("imp" + String(j)).className = "importancebtn btn mr-1";
                    }
                }
            }
        }
    });


    $(".hovercard").on('click', function () {
        var itemId = this.id;
        itemId = itemId.slice(15)
        if ($("#description" + itemId).css("display") == "none") {
            $("#description" + itemId).show(300);
            var temp = document.getElementById("descriptionicon" + itemId);
            temp.className = "bootstrap-icons bi-arrow-up-short"
        } else {
            $("#description" + itemId).hide(300);
            var temp = document.getElementById("descriptionicon" + itemId);
            temp.className = "bootstrap-icons bi-arrow-down-short"
        }

    });

    $(".categories").hover(function () {
        $(this).find(".delete-category").show();
    }, function () {
        $(this).find(".delete-category").hide()
    });


    $("#new-item").click(function () {
        var element = document.getElementById("toast-b");
        if ($("#category-select").val() == null) {
            element.innerHTML = "Please select the category!";
            $('.toast').toast('show');
        } else if ($("#item-input").val() == '') {
            element.innerHTML = "To Do is empty!";
            $('.toast').toast('show');
        } else if (parseInt($("#items-count").html(), 10) >= 15) {
            element.innerHTML = "There are too many categories!";
            $('.toast').toast('show');
        } else {
            var element_h = document.getElementById("toast-h");
            element_h.innerHTML = "Great";
            element.innerHTML = "Add the item successfully!";
            $('.toast').toast('show');
            document.getElementById('add-item-form').submit();
        }
    });

    $("#new-category").click(function () {
        var element = document.getElementById("toast-b");
        if ($("#category-input").val() == '') {
            element.innerHTML = "The name is empty!";
            $('.toast').toast('show');
        } else if (parseInt($("#category-count").html(), 10) >= 12) {
            element.innerHTML = "There are too many categories!";
            $('.toast').toast('show');
        } else {
            var element_h = document.getElementById("toast-h");
            element_h.innerHTML = "Great";
            element.innerHTML = "Add the category successfully!";
            $('.toast').toast('show');
            document.getElementById('add-category-form').submit()
        }
    });



    $(".item-done").click(function () {
        var element = document.getElementById("toast-b");
        var element_h = document.getElementById("toast-h");
        element_h.innerHTML = "Great";
        $(this).parent().slideUp();
        element.innerHTML = "Well!";
        $('.toast').toast('show');
    });

    $(".categories").hover(function () {
        $(this).find(".delete-category").show();
    }, function () {
        $(this).find(".delete-category").hide()
    });

    $(".categories").hover(function () {
        $(this).find(".change-icon").show();
    }, function () {
        $(this).find(".change-icon").hide()
    });

    $("#icon1").click(function () {
        var todo_icon = document.getElementById("todo-icon");
        todo_icon.className = "bootstrap-icons bi-check2-circle float-left";
    });
    $("#icon2").click(function () {
        var todo_icon = document.getElementById("todo-icon");
        todo_icon.className = "bootstrap-icons bi-cart3 float-left";
    });
    $("#icon3").click(function () {
        var todo_icon = document.getElementById("todo-icon");
        todo_icon.className = "bootstrap-icons bi-caret-up float-left";
    });
    $("#icon4").click(function () {
        var todo_icon = document.getElementById("todo-icon");
        todo_icon.className = "bootstrap-icons bi-camera float-left";
    });
    $("#icon5").click(function () {
        var todo_icon = document.getElementById("down-icon");
        todo_icon.className = "bootstrap-icons bi-check2-circle float-left";
    });
    $("#icon6").click(function () {
        var todo_icon = document.getElementById("down-icon");
        todo_icon.className = "bootstrap-icons bi-cart3 float-left";
    });
    $("#icon7").click(function () {
        var todo_icon = document.getElementById("down-icon");
        todo_icon.className = "bootstrap-icons bi-caret-up float-left";
    });
    $("#icon8").click(function () {
        var todo_icon = document.getElementById("down-icon");
        todo_icon.className = "bootstrap-icons bi-camera float-left";
    });

    $("#icon10").click(function () {
        var todo_icon = document.getElementById("down-icon");
        todo_icon.className = "stars";
    });

    $(".confirm-btn").click(function () {
        var element = document.getElementById("toast-b");
        var element_h = document.getElementById("toast-h");
        element_h.innerHTML = "Great";
        element.innerHTML = "Modify Successfully!";
        $('.toast').toast('show');
    });

    $(".delete-item").click(function () {
        var element = document.getElementById("toast-b");
        var element_h = document.getElementById("toast-h");
        element_h.innerHTML = "Great";
        $(this).parent().slideUp();
        element.innerHTML = "Delete Successfully!";
        $('.toast').toast('show');
    });

    $(".delete-category").click(function () {
        var element = document.getElementById("toast-b");
        var element_h = document.getElementById("toast-h");
        element_h.innerHTML = "Great";
        $(this).parent().slideUp();
        element.innerHTML = "Delete Successfully!";
        $('.toast').toast('show');
    });

    $("#login-btn").click(function () {

        document.getElementById('login-form').submit()

    });
    $("#inputDate").datepicker({
        format: 'yyyy-mm-dd',
        autoclose: true,
        todayBtn: 1,
        autoclose: 1,
        minView: 0,
        clearBtn: true,
        todayHighlight: true,
    });

})