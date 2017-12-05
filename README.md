# restAPI
https://medium.com/python-rest-api-toolkit/build-a-python-rest-api-in-5-minutes-c183c00d3465 </br>
https://python-scripts.com/build-rest-api
<p>В этой статье мы рассмотрим новый фреймворк <strong>Arrested</strong>, который используется для создания <strong>REST API</strong> при помощи Python. Мы используем <strong>Docker</strong>, <a href="https://python-scripts.com/database">SQLAlchemy</a> и прочие инструменты для создания API на тему <em>Звездных Войн</em> всего за пять минут!</p>
<p>Это первый пост в серии в будущей серии статей, нацеленных на помощь людям в построении <a href="https://python-scripts.com/build-rest-api">REST API Python</a>. Мы собрали коллекцию инструментов, которые помогут вам быстро начать и не слишком напрягаться на протяжении работы. В данном материале мы представим вам фреймворк <a href="https://github.com/mikeywaites/flask-arrested">Arrested</a>, который используется для создания API при помощи <a href="https://python-scripts.com/flask-vs-django">Flask</a>. Данный фреймворк нацелен сделать создание <strong>REST API</strong> безболезненным процессом. Подходит для быстрого использования в проектах, при этом легко расширяется для особых требований.</p>
<h2>В данной статье мы рассмотрим</h2>
<ol>
<li>Использование <strong>Cookie Cutter</strong> шаблона для установки приложения Flask вместе с базой данных <strong>SQLAlchemy ORM</strong> для взаимодействия с базой данных, <strong>Kim Mappers</strong> для сериализации и сортировки, хранилище <strong>Docker</strong> для среды разработки и пример пользовательского API;</li>
<li>Создание ресурсов на тему <em>Звездных Войн</em>, для получения списков персонажей, создания новых персонажей, поиск персонажей по ID и наконец, обновление и удаление персонажа.</li>
</ol>
<h3>Список ресурсов инструментов, которые мы будем использовать</h3>
<ul>
<li><a href="http://docker.com/">Docker</a> – используется во всех наших примерах;</li>
<li><a href="https://git-scm.com/">Git</a> – для клонирования некоторых хранилищ;</li>
<li><a href="http://cookiecutter.readthedocs.io/en/latest/">Cookie Cutter</a> – инструмент для создания проектных шаблонов;</li>
<li><a href="http://flask.pocoo.org/">Flask</a> – наш фреймворк Arrested работает на <strong>Flask</strong>, микро-фреймворке для Python, который в свою очередь базируется на Werkzeug;</li>
<li><a href="http://kim.readthedocs.io/en/latest/">Kim</a> – фреймворк Python для сортировки и сериализации;</li>
<li><a href="https://arrested.readthedocs.org/">Arrested</a> – фреймворк для быстрого создания API при помощи Flask</li>
</ul>
