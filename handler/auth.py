
'''
实现登录功能的handler
'''

from tornado.web import RequestHandler

from tornado.websocket import WebSocketHandler

# tornado没有内置session
from pycket.session import SessionMixin

# 账户信息是否正确
from util.auth import authenticate, regist, is_exsist_user


# 有身份验证功能的basehandler
class AuthBaseHandler(RequestHandler, SessionMixin):
    def get_current_user(self):
        current_user = self.session.get('user_ID')
        if current_user:
            return current_user

        return None


# 声明websocket基类, 采用websocket协议
class AuthBaseWebSocketHandler(WebSocketHandler, SessionMixin):
    def get_current_user(self):
        current_user = self.session.get('user_ID')
        if current_user:
            return current_user

        return None


# 实现登陆功能
class LoginHandler(AuthBaseHandler):
    def get(self, *args, **kwargs):
        next_name = self.get_argument('next', '/')
        self.render(
            template_name="login.html",
            nextname=next_name,
        )

    def post(self, *args, **kwargs):
        telephone = self.get_argument('telephone')
        password = self.get_argument('password')

        # 手机号码和密码都非空时
        if telephone and password:
            flag = authenticate(telephone, password)

            # 若账户信息正确
            if flag:

                # 利用session存储用户登录信息
                self.session.set('user_ID', telephone)

                # 设置加密cookie，保持登录状态, 不推荐使用
                # self.set_secure_cookie('user_ID', user)

                # 获取之前访问的路由
                next_name = self.get_argument('next', '')

                # 返回之前访问的页面
                self.redirect(next_name)

            else:
                self.write('fail to login, check the account')

        else:
            self.write('fail to login, check the account')



# 实现登出功能, 即注销账号
class LoginOutHandler(AuthBaseHandler):
    def get(self, *args, **kwargs):
        self.session.delete('user_ID')
        self.redirect('/login')


# 注册功能
class RegistHandler(AuthBaseHandler):
    def get(self, *args, **kwargs):
        msg = self.get_argument('msg', None)
        self.render(
            template_name='regist.html',
            msg=msg,
        )


    def post(self, *args, **kwargs):
        username = self.get_argument('username', '')
        telephone = self.get_argument('telephone', '')
        password1 = self.get_argument('password1')
        password2 = self.get_argument('password2')


        # 检查两次密码是否相同
        if password1 == password2:
            ret = regist(username=username, telephone=telephone, raw_password=password2)

            if ret['msg'] == 'ok':

                # 保存账户信息，保持其登录状态
                self.session.set('user_ID', telephone)

                # 跳转回主页
                self.redirect('/')
            else:
                self.redirect('/regist?msg={}'.format(ret))

        else:
            self.write('Two passwords are inconsistent. Please check them.')

