<template>
    <div class="contact-area ptb-80 pt-0">
        <div class="container">
            <div class="section-title">
                <h2>Get In Touch With Us</h2>
                <div class="bar"></div>
                <p>Anything On your Mind. We’ll Be Glad To Assist You!</p>
            </div>

            <div class="row h-100 justify-content-center align-items-center">
                <div class="col-lg-6 col-md-12">
                    <img src="~/assets/img/1.png" alt="image">
                </div>

                <div class="col-lg-6 col-md-12">
                    <form id="contactForm">
                        <div class="row">
                            <div class="col-lg-12 col-md-12">
                                <div class="form-group">
                                    <input type="text" name="name" id="name" class="form-control" placeholder="Name">
                                </div>
                            </div>

                            <div class="col-lg-12 col-md-12">
                                <div class="form-group">
                                    <input type="email" name="email" id="email" class="form-control" placeholder="Email">
                                </div>
                            </div>

                            <div class="col-lg-12 col-md-6">
                                <div class="form-group">
                                    <input type="text" name="phone_number" id="phone_number" class="form-control" placeholder="Phone">
                                </div>
                            </div>

                            <div class="col-lg-12 col-md-6">
                                <div class="form-group">
                                    <input type="text" name="msg_subject" id="msg_subject" class="form-control" placeholder="Subject">
                                </div>
                            </div>

                            <div class="col-lg-12 col-md-12">
                                <div class="form-group">
                                    <textarea name="message" class="form-control" id="message" cols="30" rows="5" placeholder="Your Message"></textarea>
                                </div>
                            </div>

                            <div class="col-lg-12 col-md-12">
                                <button type="submit" class="btn btn-primary">Send Message</button>
                                <div id="msgSubmit" class="h3 text-center hidden"></div>
                                <div class="clearfix"></div>
                            </div>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'ContactArea'
}
</script>