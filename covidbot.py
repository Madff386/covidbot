import discord
from discord.ext import commands
import urllib.request, urllib.error, urllib.parse


def query(thing):
	url = 'https://www.dhhs.vic.gov.au/victorian-coronavirus-covid-19-data'

	response = urllib.request.urlopen(url)
	webContent = response.read()
	webContent = str(webContent)

	if thing == 'cases':
		index = webContent.find('<p>cases acquired locally<br>(last 24 hours)<br><br></p>')
		cases_24h = webContent[index-100:index]
		start = cases_24h.find('<h4>')
		end = cases_24h.find('</h4>')
		cases_24h = cases_24h[start+4:end]

		index = webContent.find('<p>internationally acquired &<br> in quarantine<br>(last 24 hours)</p>')
		cases_quarantine = webContent[index-100:index]
		start = cases_quarantine.find('<h4>')
		end = cases_quarantine.find('</h4>')
		cases_quarantine = cases_quarantine[start+4:end]

		index = webContent.find('<p>active cases</p>')
		cases_active = webContent[index-100:index]
		start = cases_active.find('<h4>')
		end = cases_active.find('</h4>')
		cases_active = cases_active[start+4:end]

		return cases_24h, cases_quarantine, cases_active




TOKEN = 'Nzk4MTMxMzE2NjI0NDU3NzU4.X_wjtg.-DD0Xl6B1xmJ4oeR_m8_ufz1vuk'


bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
	print(f'{bot.user.name} has connected to Discord!')
	for guild in bot.guilds:
		print(f'{bot.user.name} is connected to the following guild:\n'
		f'{guild.name}(id: {guild.id})')
	
@bot.command(name='cases')
async def covid_cases(ctx):
	cases = query('cases')
	response = f'Cases acquired locally (last 24 hours): {cases[0]}\nInternationally acquired (last 24 hours): {cases[1]}\nActive cases: {cases[2]}'
	await ctx.send(response)


bot.run(TOKEN)
