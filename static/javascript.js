Dropzone.options.myAwesomeDropzone = {
    paramName: "input", // The name that will be used to transfer the file
    maxFilesize: 2, // MB
    accept: function (file, done) {
        console.log(file);
        done("");
    },

    init: function () {
        this.on("success", function (file, response) {
            console.log(response)

            $("#result").append(response);
        });
    }
};