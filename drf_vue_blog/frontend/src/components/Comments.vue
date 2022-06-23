
<script>
  import axios from 'axios';
  import authorization from '@/utils/authorization';

  export default {
    name: 'Comments',

    props: { article: Object },
    data: function () {
      return {

        comments: [],

        message: '',
        placeholder: '说点啥吧...',

        parentID: null
      }
    },

    watch: {
      article() {
        this.comments = this.article !== null ? this.article.comments : []
      }
    },
    methods: {

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
    }
  }
</script>

