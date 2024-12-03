document.addEventListener('DOMContentLoaded', function () {
    var inputs = document.querySelectorAll('.inp');

    for (var i = 0; i < inputs.length; i++) {
        inputs[i].addEventListener('input', function () {
            var maxLength = parseInt(this.getAttribute('maxlength'));
            var currentLength = this.value.length;

            if (currentLength >= maxLength) {
                var nextInput = this.nextElementSibling;
                if (nextInput !== null) {
                    nextInput.focus();
                }
            }
        });

        inputs[i].addEventListener('keydown', function (e) {
            if (e.key === 'Backspace' && this.value.length === 0) {
                var previousInput = this.previousElementSibling;
                if (previousInput !== null) {
                    previousInput.focus();
                }
            }
        });
    }
});


