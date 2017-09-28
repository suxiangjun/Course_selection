## 项目名称：选课系统

#### 实现功能:

- 创建北京、上海 2 所学校
- 创建linux , python , go 3个课程 ， linux\py 在北京开， go 在上海开
- 课程包含，周期，价格，通过学校创建课程   ok
- 通过学校创建班级， 班级关联课程、讲师
- 创建学员时，选择学校，关联班级
- 创建讲师角色时要关联学校，
- 提供两个角色接口
-   1 学员视图， 可以注册， 交学费， 选择班级，
-   2 讲师视图， 讲师可管理自己的班级， 上课时选择班级， 查看班级学员列表 ， 修改所管理的学员的成绩
-   3 管理视图，创建讲师， 创建班级，创建课程
- 上面的操作产生的数据都通过pickle序列化保存到文件里

#### 程序架构

```php+HTML
Course_selection
├──Course_selection             # atm 主程目录
│      ├──bin                   #  执行文件目录
│      │   ├──select_course.py  # 执行程序
│      │   └──init.py
│      ├──conf                  # 配置文件
│      │   ├──student_account.conf
│      │   ├──teacher_account.conf
│      │   └──init.py
│      ├──core                  # 主要程序逻辑 都在这个目录里
│      │   ├──admin.py             # 管理员模块
│      │   ├──main.py              # 主逻辑交互程序
│      │   ├──models.py            # 所有的类
│      │   ├──student.py           # 学员模块
│      │   ├──teacher.py           # 讲师模块
│      │   └──init.py
│      ├──db                     # 用户数据存储的地方
│      │   ├──class                    # 班级数据目录
│      │   ├──course                   # 课程数据目录
│      │   ├──school                   # 学校数据目录
│      │   ├──student                  # 学生数据目录
│      │   ├──teacher                  # 讲师数据目录
│      │   └──init.py
│      ├──readme.md
│      └──init.py
```

**注：q返回上一层，b退出程序**

`博客地址:`http://www.cnblogs.com/xiangjun555





