from flask import Flask, render_template, request
from target_dict import TARGETS
from synthesis import synthesis


app = Flask(
    import_name=__name__,
    instance_relative_config=True,
    static_url_path="/",
    static_folder='client/',
    template_folder='client/'
)

@app.route("/")
def hello_world():
    return render_template('index.html')


@app.route("/conversion/single/<target>", methods=["POST"])
def voice_conversion(target):
    file = request.files['voice']
    file.save("./input.wav")
    
    if target not in TARGETS:
        return {'result': "no target"}, 400
    
    target = TARGETS[target]
    synthesis(
        "./input.wav", 
        "./example/%s" % target, 
        './client/output.wav'
    )
    return {'result': "success"}


@app.route("/conversion/dual", methods=['POST'])
def voice_conversion_dual():
    src_file = request.files['voice1']
    tgt_file = request.files['voice2']
    src_file.save("./input1.wav")
    tgt_file.save("./input2.wav")

    synthesis(
        "./input1.wav", 
        "./input2.wav", 
        './client/output.wav'
    )
    return {'result': 'success'}


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')