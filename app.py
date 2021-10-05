from flask import Flask, render_template, request
from target_dict import TARGETS
from synthesis import synthesis
from string import ascii_letters
from random import choice


app = Flask(
    import_name=__name__,
    instance_relative_config=True,
    static_url_path="/",
    static_folder='client/',
    template_folder='client/'
)


def get_random_id():
    """Get Random String for Identification"""
    string_pool = ascii_letters + "0123456789"
    rand_string = [choice(string_pool) for _ in range(15)]
    return "".join(rand_string)



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

    output_name = get_random_id()

    synthesis(
        "./input.wav", 
        "./example/%s" % target, 
        './client/%s.wav' % output_name
    )
    return {'result': '/%s.wav' % output_name}


@app.route("/conversion/dual", methods=['POST'])
def voice_conversion_dual():
    src_file = request.files['voice1']
    tgt_file = request.files['voice2']
    src_file.save("./input1.wav")
    tgt_file.save("./input2.wav")

    output_name = get_random_id()

    synthesis(
        "./input1.wav", 
        "./input2.wav", 
        './client/%s.wav' % output_name
    )
    return {'result': '/%s.wav' % output_name}


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')