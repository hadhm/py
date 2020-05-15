### query
1. func: sum,count,avg,min,max
2. filter(User.id==1)
3. filter_by(id=1)


### sqlalchemy中的orm
ForeignKey中的ondelete是数据库层面，而非orm层面
1. restrict 不允许删除有父键关联的
2. set null 置null(类似于orm中默认)
3. cascade 删除(类似于orm中的delete)

如将数据库外键加参restrict，在orm层面，删除父表数据，则从表中会置null，如要orm层面阻止，则Column中设置nullable=False

将数据添加到session中，和它相关的数据一起存入，是通过relationship中的cascade参数设置的：
1. save-update 默认选项，添加时将相关数据一起添加
2. delete 删除一个模型的数据时，是否也删掉relationship相关的数据
3. delete-orphan 一个orm对象解除了父表中的关联对象时，自己便会被删除，只能用于一对多，不能用于多对多和一对一，还要在子模型的relactionship中加上single_parent=True的值
4. merge 默认选项，使用session.merge合并对象时，relationship相关对象也会进行
5. expunge 移除操作时，相关联对象也进行移除，只在session中移除，数据库层面不会操作
6. all save-update,merge,reresh-expire,expunge,delete几种的缩写


### sqlalchemy的order_by
1. articles = session.query(DemoArticle).order_by(DemoArticle.id.desc()).all()
2. __mapper_args__ = {
    'order_by': id,
  }


### limit,offset,slice
1. articles = session.query(DemoArticle).order_by(DemoArticle.id.desc()).slice(0, 10).all()
2. articles = session.query(DemoArticle).order_by(DemoArticle.id.desc())[0:10]


### 懒加载
1. articles = relationship('DemoArticle', cascade='save-update,delete', lazy='dynamic')
2. u.articles is sqlalchemy.orm.dynamic.AppenderQuery
u = session.query(DemoUser).get(1)
print(u.articles.filter(DemoArticle.id == 2).all())
3. u.articles.append(Article)正常使用，访问了属性就会触发读数据库


### group_by, having


### join
1. 默认是inner join
result = session.query(User.username,func.count(Article.id)).join(Article,User.id==Article.user_id).group_by(User.id).order_by(func.count(Article.id).desc())
print(result)


### subquery
  stmt = session.query(
      User.username.label('username'),
      User.age.label('age')).filter(User.username == '张三').subquery()
  print(type(stmt))
  '''
  <class 'sqlalchemy.sql.selectable.Alias'>
  result = session.query(User).filter(User.username.like(f'{"张三"[:1]}%'))
  '''
  result = session.query(User).filter(User.username == stmt.c.username,
                                      User.age == stmt.c.age)
  print(result)
