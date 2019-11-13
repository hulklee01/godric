Vue.component('power', {
    template: '<h1>I wanna Test</h1>'
})

var app = new Vue({
    el: '#app',
    data: {
        message: 'Hi Yummy!!'
    }
})

var app2 = new Vue({
    el: '#app2',
    data: {
        message: 'You can see me'
    }
})

var app3 = new Vue({
    el: '#app-3',
    data: {
        seen: true
    }
})

var app4 = new Vue({
    el: '#app-4',
    data: {
        mans: [
            { fn: 'oh'},
            { fn: 'jo'},
            { fn: 'je'}
        ]
    }
})

var app5 = new Vue({
    el: '#app-5',
    data:{
        message: 'Hello'
    },
    methods:{
        changeMes: function () {
            this.message = 'Hi!'
        }
    }
})

var app6 = new Vue({
    el: '#app-6',
    data: {
        message: 'Where am I??'
    }
})