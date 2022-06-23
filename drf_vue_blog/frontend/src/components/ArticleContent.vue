<template>
<div>
    <div v-if="article !== null" id="content">
        <div id="center-content">
            <h1 id="title">{{ article.title }}</h1>
            <p id="subtitle">
                本文由 {{ article.author.username }} 发布于 {{ formatted_time(article.created) }}
                <span v-if="isSuperuser">
                <router-link :to="{ name: 'ArticleEdit', params: { id: article.id }}">
                    更新与删除
                </router-link>
                </span>
            </p>
            <div v-html="article.body_html" class="article-body" ></div>
        </div>
        <div id="menu-content">
            <div id="menu-kernel">
                <h3 id="menu-title">目录</h3>
                <div v-html="article.toc_html" class="toc"></div>
            </div>
        </div>
    </div>


    <div id="comment">
    <br><br>
    <hr>
    <h3>发表评论</h3>

    <textarea
                v-model="message"
                :placeholder="placeholder"
                name="comment"
                id="comment-area"
                cols="60"
                rows="10"
                ></textarea>
    <div>
        <button @click="submit" class="submitBtn">发布</button>
    </div>

    <br>
    <p>已有 {{ comments.length }} 条评论</p>
    <hr>

    <div
        v-for="comment in comments"
        :key="comment.id"
        >
        <div class="comments">
        <div>
            <span class="username">
            {{ comment.author.username }}
            </span>
            于
            <span class="created">
            {{ formatted_time(comment.created) }}
            </span>
            <span v-if="comment.parent">
            对
            <span class="parent">
                {{ comment.parent.author.username }}
            </span>
            </span>
            说道：
        </div>
        <div class="content">
            {{ comment.content }}
        </div>
        <div>
            <button class="commentBtn" @click="replyTo(comment)">回复</button>
        </div>
        </div>
        <hr>
    </div>
    </div>

</div>
</template>

<script>

    import axios from 'axios';
    import authorization from '@/utils/authorization';

    export default {

        data: function () {
            return {
                article: null,
                comments: [],
                message: '',
                placeholder: '说点啥吧...',
                parentID: null
            }
        },
        watch: {
            article() {
                this.comments = this.article !== null ? this.article.comments : []
            },
        },
        mounted() {
            axios
                .get('/api/article/' + this.$route.params.id)
                .then(response => (this.article = response.data))
        },
        methods: {
            formatted_time: function (iso_date_string) {
                const date = new Date(iso_date_string);
                return date.toLocaleDateString()
            },

            submit() {
                const that = this;
                authorization()
                .then(function (response) {
                    if (response[0]) {
                    axios
                        .post('/api/comment/',
                        {
                            content: that.message,
                            article_id: that.article.id,
                            parent_id: that.parentID,
                        },
                        {
                            headers: {Authorization: 'Bearer ' + localStorage.getItem('access.myblog')}
                        })
                        .then(function (response) {

                        that.comments.unshift(response.data);
                        that.message = '';
                        alert('留言成功')
                        })
                    }
                    else {
                    alert('请登录后评论。')
                    }
                })
            },
            replyTo(comment) {
                this.parentID = comment.id;
                this.placeholder = '对' + comment.author.username + '说:'
            },

            formatted_time: function (iso_date_string) {
                const date = new Date(iso_date_string);
                return date.toLocaleDateString() + '  ' + date.toLocaleTimeString()
            },
        },
        computed: {
            isSuperuser() {
            return localStorage.getItem('isSuperuser.myblog') === 'true'
            }
        }
    }

</script>

<style scoped>
    #content{
        display: block;
        margin-left: 260px;
        position: relative;
        height: auto;
        overflow: hidden;
        z-index: 0;
    }

    #center-content{
        float: left;
        margin-left: 0;
        margin-top: 0;
        width: 70%;
    }

    #menu-content{
        position: fixed;
        display: inline;
        top: 160px;
        left: 260px+70%;
        height: 500px;

        width: 300px;
        background-color: whitesmoke;
    }

    #menu-kernel{
        float: left;
        height: 100%;
        width: 100%;
        overflow-x: hidden;
        overflow-y: scroll;
        scrollbar-width: none;
        scroll-behavior: auto;
    }

    #menu-title{
        text-align: center;
    }

    #title {
        text-align: center;
        font-size: x-large;
    }

    #subtitle {
        text-align: center;
        color: gray;
        font-size: small;
    }




</style>

<style>



    .toc ul {
        list-style-type: none;
    }

    .toc a {
        color: gray;
        text-decoration: none;
        font-size: 20px;
        font-style: italic;
    }

    .article-body{
        margin: 0 50px;
        /* white-space:normal;
        word-break:break-all;
        word-wrap:break-word;  */
        overflow-x: scroll;
        overflow-y: hidden;
        background-color: white;
        font-style: normal;
        font-family: Arial, Helvetica, sans-serif;
    }

    .article-body p img {
        max-width: 100%;
        border-radius: 50px;
        box-shadow: gray 0 0 20px;
    }

    .codehilite{
        font-size: large;
    }

    pre{
        margin: 20px 20px;
        overflow-x: scroll;
        overflow-y: hidden;
    }


</style>


<style scoped>

  #comment {
    margin-left: 280px;
    width: 50%;
  }

  button {
    cursor: pointer;
    border: none;
    outline: none;
    color: whitesmoke;
    border-radius: 5px;
  }
  .submitBtn {
    height: 35px;
    background: steelblue;
    width: 60px;
  }
  .commentBtn {
    height: 25px;
    background: lightslategray;
    width: 40px;
  }
  .comments {
    padding-top: 10px;
  }
  .username {
    font-weight: bold;
    color: darkorange;
  }
  .created {
    font-weight: bold;
    color: darkblue;
  }
  .parent {
    font-weight: bold;
    color: orangered;
  }
  .content {
    font-size: large;
    padding: 15px;
  }
</style>


<style>

pre { line-height: 125%; }
td.linenos .normal { color: inherit; background-color: transparent; padding-left: 5px; padding-right: 5px; }
span.linenos { color: inherit; background-color: transparent; padding-left: 5px; padding-right: 5px; }
td.linenos .special { color: #000000; background-color: #ffffc0; padding-left: 5px; padding-right: 5px; }
span.linenos.special { color: #000000; background-color: #ffffc0; padding-left: 5px; padding-right: 5px; }
.hll { background-color: #ffffcc }
.c { color: #3D7B7B; font-style: italic } /* Comment */
/* .err { border: 1px solid #FF0000 } Error */
.k { color: #008000; font-weight: bold } /* Keyword */
.o { color: #666666 } /* Operator */
.ch { color: #3D7B7B; font-style: italic } /* Comment.Hashbang */
.cm { color: #3D7B7B; font-style: italic } /* Comment.Multiline */
.cp { color: #9C6500 } /* Comment.Preproc */
.cpf { color: #3D7B7B; font-style: italic } /* Comment.PreprocFile */
.c1 { color: #3D7B7B; font-style: italic } /* Comment.Single */
.cs { color: #3D7B7B; font-style: italic } /* Comment.Special */
.gd { color: #A00000 } /* Generic.Deleted */
.ge { font-style: italic } /* Generic.Emph */
.gr { color: #E40000 } /* Generic.Error */
.gh { color: #000080; font-weight: bold } /* Generic.Heading */
.gi { color: #008400 } /* Generic.Inserted */
.go { color: #717171 } /* Generic.Output */
.gp { color: #000080; font-weight: bold } /* Generic.Prompt */
.gs { font-weight: bold } /* Generic.Strong */
.gu { color: #800080; font-weight: bold } /* Generic.Subheading */
.gt { color: #0044DD } /* Generic.Traceback */
.kc { color: #008000; font-weight: bold } /* Keyword.Constant */
.kd { color: #008000; font-weight: bold } /* Keyword.Declaration */
.kn { color: #008000; font-weight: bold } /* Keyword.Namespace */
.kp { color: #008000 } /* Keyword.Pseudo */
.kr { color: #008000; font-weight: bold } /* Keyword.Reserved */
.kt { color: #B00040 } /* Keyword.Type */
.m { color: #666666 } /* Literal.Number */
.s { color: #BA2121 } /* Literal.String */
.na { color: #687822 } /* Name.Attribute */
.nb { color: #008000 } /* Name.Builtin */
.nc { color: #0000FF; font-weight: bold } /* Name.Class */
.no { color: #880000 } /* Name.Constant */
.nd { color: #AA22FF } /* Name.Decorator */
.ni { color: #717171; font-weight: bold } /* Name.Entity */
.ne { color: #CB3F38; font-weight: bold } /* Name.Exception */
.nf { color: #0000FF } /* Name.Function */
.nl { color: #767600 } /* Name.Label */
.nn { color: #0000FF; font-weight: bold } /* Name.Namespace */
.nt { color: #008000; font-weight: bold } /* Name.Tag */
.nv { color: #19177C } /* Name.Variable */
.ow { color: #AA22FF; font-weight: bold } /* Operator.Word */
.w { color: #bbbbbb } /* Text.Whitespace */
.mb { color: #666666 } /* Literal.Number.Bin */
.mf { color: #666666 } /* Literal.Number.Float */
.mh { color: #666666 } /* Literal.Number.Hex */
.mi { color: #666666 } /* Literal.Number.Integer */
.mo { color: #666666 } /* Literal.Number.Oct */
.sa { color: #BA2121 } /* Literal.String.Affix */
.sb { color: #BA2121 } /* Literal.String.Backtick */
.sc { color: #BA2121 } /* Literal.String.Char */
.dl { color: #BA2121 } /* Literal.String.Delimiter */
.sd { color: #BA2121; font-style: italic } /* Literal.String.Doc */
.s2 { color: #BA2121 } /* Literal.String.Double */
.se { color: #AA5D1F; font-weight: bold } /* Literal.String.Escape */
.sh { color: #BA2121 } /* Literal.String.Heredoc */
.si { color: #A45A77; font-weight: bold } /* Literal.String.Interpol */
.sx { color: #008000 } /* Literal.String.Other */
.sr { color: #A45A77 } /* Literal.String.Regex */
.s1 { color: #BA2121 } /* Literal.String.Single */
.ss { color: #19177C } /* Literal.String.Symbol */
.bp { color: #008000 } /* Name.Builtin.Pseudo */
.fm { color: #0000FF } /* Name.Function.Magic */
.vc { color: #19177C } /* Name.Variable.Class */
.vg { color: #19177C } /* Name.Variable.Global */
.vi { color: #19177C } /* Name.Variable.Instance */
.vm { color: #19177C } /* Name.Variable.Magic */
.il { color: #666666 } /* Literal.Number.Integer.Long */


</style>