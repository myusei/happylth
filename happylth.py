import requests
from bs4 import BeautifulSoup

class Happylth:
	## 変数 ##

	# happylthのURL
	sso_root_url = 'https://happylth.com'
	happylth_root_url = 'https://point.happylth.com'

	# ユーザー情報
	user = ''
	password = ''
	company_path = ''

	# セッション情報
	session = requests.session()

	# happlth内のデータを格納する辞書
	__param = dict()


	## 関数 ##

	def __init__(self, user, password, company_path):
		self.user = user
		self.password = password
		self.company_path = company_path

		try:
			self.login()
		except:
			raise Exception('ログインに失敗しました')

	def __make_tag_name(self, key):
		return f"_bohcchallengeinputrecord_WAR_BOHCChallengeportlet_{key}"

	def __set_dict(self, soup, key, tagName=None):
		if not tagName:
			tagName = self.__make_tag_name(key)
		self.__param[key] = soup.find('input', attrs={'name': tagName})['value']

	def __get_inputrecord(self):
		try:
			res = self.session.get(self.happylth_root_url + self.company_path + '/inputrecord')
			if res.status_code != 200:
				raise
		except:
			raise Exception('Requests Error: Failed get inputrecord')

		try:
			soup = BeautifulSoup(res.text)
			self.__param['url'] = soup.find('form')['action']
			self.__set_dict(soup, 'formDate')
			self.__set_dict(soup, 'sysDate')
			self.__set_dict(soup, 'isSelfControl')
			self.__set_dict(soup, 'dateFromParam')
			self.__set_dict(soup, 'recordDiv')
			self.__set_dict(soup, 'runningNum')
			self.__set_dict(soup, 'walkingDivNM')
			self.__set_dict(soup, 'lifestyleDivNM')
			self.__set_dict(soup, 'weightDivNM')
			self.__set_dict(soup, 'bloodPressureNM')
			self.__set_dict(soup, 'bloodSugarDivNM')
			self.__set_dict(soup, 'muscleDivNM')
			self.__set_dict(soup, 'joggingDivNM')
			self.__set_dict(soup, 'recordOmronGetFlg')
			self.__set_dict(soup, 'targetModifyFlg')
			self.__set_dict(soup, 'targetBaseDate')
			self.__set_dict(soup, 'dateRange')
			self.__set_dict(soup, 'walkCount', tagName=self.__make_tag_name('walkCountHd'))
			self.__set_dict(soup, 'walkCountHd')
			self.__set_dict(soup, 'walkCountNew')
			self.__set_dict(soup, 'walkMemo', tagName=self.__make_tag_name('walkMemoHd'))
			self.__set_dict(soup, 'walkMemoHd')
			self.__set_dict(soup, 'radio0')
			self.__set_dict(soup, 'radio0Hd')
			self.__set_dict(soup, 'radio1')
			self.__set_dict(soup, 'radio1Hd')
			self.__set_dict(soup, 'radio2')
			self.__set_dict(soup, 'radio2Hd')
			self.__set_dict(soup, 'lifestyleMemo', tagName=self.__make_tag_name('lifestyleMemoHd'))
			self.__set_dict(soup, 'lifestyleMemoHd')
			self.__set_dict(soup, 'weight')
			self.__set_dict(soup, 'weightHd')
			self.__set_dict(soup, 'weightNew')
			self.__set_dict(soup, 'fat')
			self.__set_dict(soup, 'fatHd')
			self.__set_dict(soup, 'fatNew')
			self.__set_dict(soup, 'girth')
			self.__set_dict(soup, 'girthHd')
			self.__set_dict(soup, 'girthNew')
			self.__set_dict(soup, 'weightMemo', tagName=self.__make_tag_name('weightMemoHd'))
			self.__set_dict(soup, 'weightMemoHd')
		except:
			raise Exception('BeautifulSoup Error')

	def login(self):
		# まず happylth.com にログインする
		data = {
		    'data[Member][login_id]' : self.user,
		    'data[Member][password]' : self.password,
		}
		try:
			res = self.session.post(self.sso_root_url + '/login', data=data)
			res = self.session.get(self.sso_root_url + '/sso/6')
			# happylth.com にログインした session を使ってポイントページにログインする
			data = {
 			   	'doActionAfterSSOLogin' : 'true',
			}
			res = self.session.get(self.happylth_root_url + self.company_path + '/home', data=data)
			if res.status_code != 200:
				raise
		except:
			raise Exception('Requests Error: Failed login')

	def generate_inputrecord_payload(self):
		self.__get_inputrecord()
		return {
			self.__make_tag_name('formDate') : self.__param['formDate'],
			self.__make_tag_name('sysDate') : self.__param['sysDate'],
			self.__make_tag_name('isSelfControl') : self.__param['isSelfControl'],
			self.__make_tag_name('dateFromParam') : self.__param['dateFromParam'],
			self.__make_tag_name('recordDiv') : self.__param['recordDiv'],
			self.__make_tag_name('runningNum') : self.__param['runningNum'],
			self.__make_tag_name('walkingDivNM') : self.__param['walkingDivNM'],
			self.__make_tag_name('lifestyleDivNM') : self.__param['lifestyleDivNM'],
			self.__make_tag_name('weightDivNM') : self.__param['weightDivNM'],
			self.__make_tag_name('bloodPressureNM') : self.__param['bloodPressureNM'],
			self.__make_tag_name('bloodSugarDivNM') : self.__param['bloodSugarDivNM'],
			self.__make_tag_name('muscleDivNM') : self.__param['muscleDivNM'],
			self.__make_tag_name('joggingDivNM') : self.__param['joggingDivNM'],
			self.__make_tag_name('recordOmronGetFlg') : self.__param['recordOmronGetFlg'],
			self.__make_tag_name('targetModifyFlg') : self.__param['targetModifyFlg'],
			self.__make_tag_name('targetBaseDate') : self.__param['targetBaseDate'],
			self.__make_tag_name('dateRange') : self.__param['sysDate'],
			self.__make_tag_name('walkCount') : self.__param['walkCount'],
			self.__make_tag_name('walkCountHd') : self.__param['walkCountHd'],
			self.__make_tag_name('walkCountNew') : self.__param['walkCountNew'],
			self.__make_tag_name('walkMemo') : self.__param['walkMemo'],
			self.__make_tag_name('walkMemoHd') : self.__param['walkMemoHd'],
			self.__make_tag_name('radio0') : self.__param['radio0'],
			self.__make_tag_name('radio0Hd') : self.__param['radio0Hd'],
			self.__make_tag_name('radio1') : self.__param['radio1'],
			self.__make_tag_name('radio1Hd') : self.__param['radio1Hd'],
			self.__make_tag_name('radio2') : self.__param['radio2'],
			self.__make_tag_name('radio2Hd') : self.__param['radio2Hd'],
			self.__make_tag_name('lifestyleMemo') : self.__param['lifestyleMemo'],
			self.__make_tag_name('lifestyleMemoHd') : self.__param['lifestyleMemoHd'],
			self.__make_tag_name('weight') : self.__param['weight'],
			self.__make_tag_name('weightHd') : self.__param['weightHd'],
			self.__make_tag_name('weightNew') : self.__param['weightNew'],
			self.__make_tag_name('fat') : self.__param['fat'],
			self.__make_tag_name('fatHd') : self.__param['fatHd'],
			self.__make_tag_name('fatNew') : self.__param['fatNew'],
			self.__make_tag_name('girth') : self.__param['girth'],
			self.__make_tag_name('girthHd') : self.__param['girthHd'],
			self.__make_tag_name('girthNew') : self.__param['girthNew'],
			self.__make_tag_name('weightMemo') : self.__param['weightMemo'],
			self.__make_tag_name('weightMemoHd') : self.__param['weightMemoHd'],
		}

	def post_inputrecord(self, data):
		header = {
	    	'Content-Type': 'application/x-www-form-urlencoded',
    		'Connection': 'keep-alive'
		}
		try:
			res = self.session.post(self.__param['url'], headers=header, data=data)
			return res
		except:
			raise Exception('Requests Error: Failed post inputrecord')
