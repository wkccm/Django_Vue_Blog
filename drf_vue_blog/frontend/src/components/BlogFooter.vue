<template>
    <div>
        <br><br><br>
        <div id="footer">
            <p id="domain"><a href="https://beian.miit.gov.cn" target="_blank">吉ICP备2022003698号-1</a></p>
            <img id="gotoTop" src="https://i02piccdn.sogoucdn.com/4f3b2858eec9e2cf" alt="" @click="gotoTop()"
                v-if="showgotoTop">
            <img id="gotoBottom" src="https://i02piccdn.sogoucdn.com/4f3b2858eec9e2cf" alt="" @click="gotoBottom()"
                v-if="showgotoBottom">
        </div>


    </div>
</template>

<script>
export default {
    name: 'BlogFooter',
    data() {
        return {
            showgotoTop: false,
            showgotoBottom: true
        }
    },
    mounted() {
        var vm = this;
        window.onscroll = function () {
            if (document.documentElement.scrollTop > 300) {
                vm.showgotoTop = true;
            }
            else {
                vm.showgotoTop = false;
            }

            if (document.documentElement.scrollTop + document.documentElement.clientHeight < document.documentElement.scrollHeight - 300) {
                vm.showgotoBottom = true;
            }
            else {
                vm.showgotoBottom = false;
            }
        }
    },
    methods: {
        gotoTop() {
            scroll(0, 0);
        },

        gotoBottom() {
            scroll(0, document.documentElement.scrollHeight);
        }
    }
}
</script>

<style scoped>
#footer {
    position: fixed;
    left: 0;
    bottom: 0;
    height: 50px;
    width: 100%;
    background: whitesmoke;
    text-align: center;
    font-weight: bold;
}

#domain {
    height: 50px;
    margin: 15px auto;
}

#gotoTop {
    position: fixed;
    right: 80px;
    bottom: 0px;
    height: 50px;
}

#gotoTop:hover {
    cursor: pointer;
}


#gotoBottom {
    position: fixed;
    right: 30px;
    bottom: 0px;
    height: 50px;
    transform: rotateX(180deg);
}

#gotoBottom:hover {
    cursor: pointer;
}
</style>
