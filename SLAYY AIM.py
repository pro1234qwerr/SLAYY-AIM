#pip install pycryptodome  , It works only v3.11.5 Above.
import random ,base64,codecs,zlib,sys;py=""
sys.setrecursionlimit(1000000000) 

pyobfuscate = (lambda **kwargs: (list(kwargs.keys()),list(kwargs.values())))(**{'https://pyobfuscate.com':'BlockingIOError * breakpoint','exec':'3bAagCdpR1rzK9RLBCOqVq1OWi2fZ46YHNutFOuauvwLssNJkYSwDfQtOVdTgjHUNwdTJueVNgi1bt0v','eval': bytes.fromhex('''ddb0b2bf8dace7f4e0f8f0fcc326eb98e115c9dc5e1ead8d19034663eeb9f60cdf3c1793d54439806e5dbbdfa9ab5b5f48857d80db0c3530242a90d36d515f28afde35ee2d90150257d104e5e59b73012db7d7bf1d5e2fa525183157698b853bce91971185098b50c0a2b2f9bb2a2bc83be3b51105e3358b88ed01f8c22617c6a60da018b684cfbc3339cdd95dd29ce8db33a8d2833219625fdb68c55750dc8fca79a4dce96f88705f4eee28a6238cdbe90c0b3a86898cbb74ebef65a5f5cddfcb70747a0256671dc2f3927ee42e020c5c469bf6254e4af7c87212ae5564df1fc1f5b9f27baaa65db53071668887d1fedf445138441ae738afe5074c93c242247cbee6079d356821ed37cc6314ebc2b3aa9c862374b3926c156b71651f61921a16c1da2ac628c5a13450dcb8fb3447decfd06a0dff72d002d770c33a8166fac70260e9e07133ef1fea33833b17d473cbe042483c7193428d48e0b397479047684977335aa7e62b4249bf8b23c11091a7bbc2358372555236b584b604899da655a6852b75d634788dd34cd4e137eda953695e791cb247cdea1c8ea1ff0b90b9ddd9a280140e540ee02d6194a0e5bf32677fc1fc0f6d7234261e681d64101e4f14628b300473c24a842559a3a7d1589de3d9d253758aff287fb53831bd226ad9fde44f7ba1aecef13a8b90fe4fdfd2209ed8d5ef0a1baaecb38fde3197b0a787d55e612bd44ca4c26643f181fd83b0b213ee1705a471c69be3e397f2bd76ea1680cd3f3a043c17d8dcfb5cd315a0a4f6c7de6ff7359378114cf21d4ac81133ebac13cf8227b245887b76121971014f728d0c57b41869feb8299cb1eb7b5fdeec5161130f4f6136184970db4d50f62a1db32616c80cd3837bff444c5a2208ea47a7aa81be7a8fd64eb08a64719e7a28801ba59dd365982898ecca17173b64c987ae57b9b89c25314c78f517e10a3121a457546eacf27ac04f7447602d793eb2bd7205a714af5f0502400305889b2f947d44d8a14857254c37391b287ce40b6519c406be5bdd2f4bf0bd197e0ba0f3f4dc3a60d8621a18971f30b8f91713cc0860e885e09c8aa97c27493ea374568b7eb04babcd1da9e27c6eabffc9e7d998518cc43c9443fd72b3fccb7eddf799e5a717e2379765040ede662ae5a02dde7c11729bb8898f8f05af343bc54c33504cee35f4de56cd59e25804f21fe830fe7df91c5df39f8d41c8db7fbe2d5f8f0a629c96b427880a2fba2a4544beab477838eb85c4e2900cf4b8b5c1c393aca47de5b2fc4c7658455c4cfa81c231fcf12efca8bf5bdd5a9d6142a7d3cec9e2cb862eda4c80752a85def7f27d74145377d42681f9253a298cb34b595b37cde483c1797cdbdf549e8916d172b4f0923587830aaa7e91f1c9fe1b9c8213be02f1eff6e7181174c407d43da849b71045de095afd4c017f47b9d6fabf13d1d0da919b7eb31c4652e68a9fd7af41461387dafcefed1183c8058b3a99c2063c320e1fb077ffc4583dc94499e297fb5b979dd753ca0a7897d3db873e84b856d14fbad4e92272746b9989a4a9999171b4f18518e53b5d3792e3d429bb57d2dac6cf30002aa22e3b96df59b7fee5964df9721010655f8353b9a7d73521ba88a3259c96a8e3cdc2bb6d29dba5453946de12b2fd5384a8f366232997d187d6c864ce873c108c34e66b212ccc8551c70079887d8a1eab8c91927e883c0d4c7abbe03469c9325a05a9d9691f6abbc320b01189b6333923d3b99950da11d05d620039fd3f012cf2fc186dae5e5d12e93aa246bad7522df35ba120a3fed9d4d450aa332f97a2b41f154f8719b06a2e4887c472d36aeefb1b244c7dbecf10e46a3f2f9414b586fec24bc16259b3c38fa2b8a5cd15d2b394e55e4502f4b1df271a985d5b2eff3226853103c1246291ba1b27b2ff712ae89cdcc4c3928d7f5f6b16d69e6437c67bc13bd2fbb633b967c5ca096e43984c49763b524a87b1067de928b97f5c0d41138790dbf4a5056914603bf129011559be6ae860a31e38f8c5300c911f80043ea8a54df29754363004d1b864b59528355955b512ba93e2cc1225b43ce80de059d46908d92831084cabd3211da54163ded2ef35ccb9ed72bb7df6479e7e0859826b3f3102b751c699a06015532a30d57567df10595cd4c90f0583a526083d7d4449577d5c662ffad89129242d2345ac1b2f6e100b8abe05d89d44eab449b1dd07e678349f4a17770570019b0e028ea784eaf22cd829bc02d60a4ddb9a56565b191f0eda689076ad7d682b1eb412932d0c8fd8e53f6271ad85bd592de98b19e37e14876a482558db573dbbca232c9ab60f2e52ae7ee875a9ab0f9c1a1624794883744920e82329f3996e3dae407e3f28e6172cd748817e9cfa902d9a086d1132ade10ae6fbf399c85808dc08ac90c72107633b606f32760092b467c85a3e455875c64efeb77c17c1ed4a4673ecd9896319b3545ce911b9ef0518e626a46fc1e3156491ed6c9e266e0be8d59cdc3ee8804c8376ec41a8077f6d2e7f9d6eba60a3eb95c93994d88c855b2f28b456004064858ddcb767af369031eae93c28615f3a35538fdb3ba140cef89b32eb71f6c1eb26b6b170b9f37121483de45dbf8d394bd356cc345e78ea2ed718d872580a23240f540918a752ce1e31e084fedddb3ca6125a58cd5178f96c7d592df591511aa017c8ada67f282a9b6e5dfd5e270336f391bccdbe72897f734021fcc86a0fc6e6ff7917140d25cfab7b509d6d0d3fbfc146c206d6146dadc50dd8a625689ffb4e50d49b408076fdc302222d7acd9b38905d62df348cc128934a22883fdbaa8be1811038a7813dfbfe67ce30d50c884d43545d07d29c4c7a095a553f792b221928d87793d25c3c4cf129b37344399ed14906645e7292108f1f9fed37bee36ed56ad547ce852489cf044d6dbc2a934504ec0c4e1ae502b997a47da869f78929198172f216020dd0c4b80a1ba257d50a24dd7349dae743596618e38f518543567be5aa8b51edc1b4c526718c3702ca2eacd41bba1c7c0163ab36d37836c97d69d19b1b14c731a4904594bd2fe77d1e86d362cc0e897ab3d84308992fd3e4696e36b71dc99e539429d528e172578b0e36f4200ce3a5e5ce2753a4b54a0ca6f7be07c3f9989855ddef80f186dce12011cbdd5ecd6ba0c0fe793d401d03ada300888f238dd92d109143e43a6e6aa4041a0533cc14681696abe02c734e25f151e0074abdb2bf37439bea6853d95902baa8aafe687ca645412439672a42e8c4a3f311551faccef47e62fb351eb84b1620d2b53b865a87f06ddbc5db0c1e7157ddb1ea10fd4d5d483f8595373bf15967fc64b5f5e3c93a177737db59080a22a0cabbfb0f6283722e1c504f711ee4b2853c61fe72ee6ad2f7719a3c901ddd598ea88b5caf4cc4588572a6fd4e5087d9c8650d4e2e9a6755f63d77c7afef4e896d1a1f2d4715937719e44bc6edc6702223b3ff939536604ef3d7b42514748458b41af3f7e8aff746d837c344a35733cbea0857
c5771ae6aa69faba4bc402a480e9ae04a5d88463b66ef43c343e75045373b4a2183567bd6855960a66eaa89ed5a2906c7e3a59b876fea114e6b2c391229bc2b629080d83ba065bd6151728fb792065913eb6d4a6273437cb23b3043ba1f8d2a8cc8859c534d5422261ec139abdbab8329920faf3e96fad40c4c3f3a5ee36132f748ff7b4764e29bbacf30f202254f3fbb0c476532d0392f44d737bc03eb3369be91a736edb96ef8e521af92dd2560f5c9d0ff2fc5666473b3327c503e176e5ae980ce5596ebc1f67d92c2d56d18b55939625ec2b53c002468fe6983ce4db91b741b01b5ab50f9bd57b8a37b531b44c0f120e86cd2b6963dd328ae8d81b000911fa09e63c1e72bc5ed446f4b8e119ff79c55d119874c151431d4f70e74fafa8ce367e1b0dc4b03cd1f643c9dab993773cf956af4ba56949b2834897a6b5176e8b022143c33c03a7887858c5bdf9266783395db9f431493b4daf2fdc7d37114e160a06b653eff6af4bfdf8146ec07da93a3bafdd5403154eb3541e67d58cb9a64277c9a4a7adcec98a32576689bd1a6fd3f0ad674f102e1757f203582f660573f60888d710d6117507ec94aaa3b2ffa5fde6c40b264126fc888e9c808b3a106ae6c6efae0f24c2526f2a934188667989d4d7b4578502a7d6f8200389a65864dad8a72f929078d802001ff0757f6f13de89f9792ffaaaf1ecaf7c623dfa1bb3db431fc3b68930d025bc8de7ed6b4c28bd970f1816167cd942809545f538686b8509becd43f61c4aa43ea48f6148b53443f0c7a266195b50eae20cf83524c78274d061832d2472d719c8804ce2d570e16be3df0cf5fff7ef71f892220dc47d49a4fa25397367f045ca0a667d02f2ca9f79b43d1a578b067112174e09630626b1c7c1084058a3cc40789ee7e70583aa4d7744e108c02812118ae1e03a17054cb6b51446f5a61faf640aa0e14c7d3437d01c3822b6635c0f7e68c5f164fe5ce937f4874b8ffbc2c058b5fb24892b0a83bfcebdd6d50491b3f3240909eee97ec4b18ba47aee5477389a917815a959cbd0c69fd2ed3785da65150621cf889276715a83731e1de6d2333a6d90453ef2339d6b9ce0c8e838ce9d8194c2a50e3377c9b201d40b7caf92fd7f7a8a70dfd338b32f9d38e60981d4f41f301af13f9e02b6c4b968e1209b856c12dfacce333907ecc915e65b5426bf79044ba86ab4b02fa9bee82dc8b693b1bb3f2eee8a99d80f7b27b02f3eaca9f6f79c1165da378e70833239f4e2d11d4973639db9ec83a22f79f6b0ffe3050ab304ecbb440d15216a0fe75d963ce7bacfc92106be6e808d1549990448c78b97d194e3e9bf58d2ad046767a9fe8536f92f4f8b82b0c89696c251a7129c77140f0434e9f720c3157f08530db0b4c13de4100d3eb01319fa9e080815265d1333eab833469ec806cb4f2ba0db8867bd64dec7617b7939b932d1948352b8c207b63afbc00dbe6d2cd26f497e5fc9f512972418bd7b2999009e6dfd2a3ea4d59b972a0d36ac09a6a20e90a7a8aa97319d76e40c8efb8b63dbde7ee35879197dd8f98f96c1d59b5737b0de1a7208057983adbb940f65f427ae035219285e28933c01c9bf6e0dd0704654c95f862b070556e034efdec047023aeedd3c136dc06fa9adf1f3e11831bf4a783345f8cef186a922f4e4a1a85aec61c4655c239ee0993a710e5c6304af7f06a5b42b54740452a97f68471a7c02d23359d3c78fbefa6cd5f234a18828d0a20cf0ff9ee10d719b6b4b7972bdccb3316a5bfd12e18663b30ed785d4557f36a9f3768ca5694496b9174ea5c19bf3dc08c66181110da4794bd716e8335e1293eac426e8af7285bc2ac1deb1b5084b5144e9c26836def6ecd620b3242e7401f181cb990e50e8b891304ae8a5a29bc8769fb94b466d7976f49bec89815cd11691ed431038c6eed50aa05eb9a05eda2fbeb83d7bec2daa73812b92af6364ab4ab35f67424b4f6cbed8c1a914b366aa337cc646d5684cb626b26e3ec907a706d072ad62fa1a0138f61193423c3237bc8fd29920e78bf2c952e7dfa7c23ba4c3fa115a168cd363a61ff79d1b13a49bdcb9d1bae4711202196eccb5beb34b7fb7b21217b2c63909f4831a3163bdb983b5ac23a1a046b4ca5211a5dee45094b820402bb2cc474886f0789b1e9c7c5b09e7997c013a62fcb8ab9d5a30a10bf42bdbb292aedae3bf6c10258d47993278807752f78254e3d043ebb74a0700082e4bbafdc0afcf2b834929d375d0db6c25d09f21f0b2408219d3f5146e9abf71222054aa32db71eb7eae15a0291338c22ab131d11a126d47222a44f8ff85e084f9d7b723df147aadb91fe6f7b9b317fdf5da768cbe23222060ad3a3f610d2e784ac1e589039a18fb84cbefbb55b9964bcabbd0a7ca026c3f7259a51e01d286121f06bd1c869d80b29642782afa0c2ad182e9c8bee4ceb8d236f56b3fa725dfe26a640ef9d3d0999c15144cf1bf0dc9dd4d775c771212b7a32351692d9b1acc544f7186608f529a8a4cbb7d00e3eab78b01af3b87a9de2f17ea7d7b4fde3d029698739d64881a029e857e1be3cdd50c491134b2819c264dad6baa2339b096e93c1fc70d316eaf79c03816a89515aaa10fd63c187b4db8e6896c506ab45a39f593a507c5be456b7799bf463fb5d7b2ab3d686a8b590cfbf9a2a76321fcf7c44dc8ba108c84f6726af0054ea7186c8a9a034a7cb0419c523fb90a37046306e7c9a14ab3dfcf4002693af583e3314513ead5819a6135d04574ee703badef841f76fcf2a813a028699ecfcb949c41069d1de3e90c1cb364a2f4a70a8f49d30228a342158635d6452384363081dc8029f8d8cd0c304a0292dfe83b4e95001efe12c42cf36370c1689a2816977474ab131af5aee05fb2b06ba7ed4c51c807ef25caa343ec8722bc23b54654fcdb20d5490c1abf671b844799b7d13fb6e30e8a658ab95172f0f7437665f5b6eecf316a8f9de93ce945519d5ab1bb57307304c96aa4fd10bda69bd63b51d9fab878a3bcd8f63be89616d98d2d838f0a7314578dad72ddc7da699162339fc2fe880aa5147f870394bfa08d6c6a05bab3ae215fd6ac03a69ecaf0927260b67419a5d11ec588faaca06020484c851c15316f85903afa557deafadca676a9a36185480297bf0efd55c898f871edde2accd7b8105ec5f2c829a0aba664799ba714ba4a1cda99c73b930b061b88745b939fb457b890d358cb8b01dfd3f2b7e35312362a0a838bc53418a591aef0e856e2e1a9da4369ff8307f3315045f6a55b99dd3e6874e91b490aed88e5667b826741160b3da2677b8e4298c8ea37b09f4b42919d1323de1e543ff811feeb4f09563b481589edfdb72d2c5ec1d2e0446af0904578c8ea6357062bf52ffb49d90e2af6c0bdca47dc09c543b4cd1a00a512ceb579fa46268d2ad9cedb6416600f7d0e9303055a7bacec5c7fa4f7e41b1d1c1004e33fd6ae7dc4f32e74771c3a34b5236e1f1c9aa0d9bbecfbfc896e99b60decd02814824bdfd82290c0af4c2f
1d81a9989e8e60c1740bd152fe01c6a76bad9940ad0930360091f560a712c53de3f9b41805b858f476aea8046b68992fbb9b2e7dbc19572de8126ce8d782e3defba976e839a830ae5a64c773b6ebe48a33eaefaa5f4433775f19a04aa7c78d8e6955a55345254f1bd77a6670ec7f58b4543d4ae69325c77234f5d088a17d43a367f74377bb8312722c4132c673b4a91f7c80bd425c27c5e269d4a779ac23da92dbc7d1dc2783ba43a377d2750c457d78bc71acd68cd8dcd806d384e4b00a55aedd55e0e41804419e33f7f9b2c2c6e495167c872138e560886c201b365ae35008b0309ca20aa1cba224f564d0645c4a2435fb394542cea3d8ca26002c56ec63408bd51f64791ad5cc0b7298af836755842ead5d1c9eda6bf4bcbb7d89b8764689504b04496f42dfd8be610219761299df0ad9b24227777b730b6856739daa0112e15a1cda41c34bdfc441f888516ba1b226dc9fbae48dbd6d918fe8737c83c89834825ba87622e272a94ea0b1d641da93d13e33f83ad576e202ae5076c6001b55be6a6493ed0f0a74ccd012532e871091026252f9c11050362586f5a119cdd4a91727b32696cfa6f20694be4c676884fa028d08784a3a0edb24cdb896de1b020e3cb4e41081abfb2b5907216ca327c9403218d90cbe425be8079a09ae3a3b4010a78fcca77a81335febc3327d1394e2c289d3ef630ffef676b631574a30e1f3356fbb9fe1dbaf5607d6e2f53880979528ededa364f87d29875319b730569cdfe4e0c8d4bd57b2c25408275decb5f16ac110b8bcdeb1b03e1ba1a1dfb8d1142f7b56adfa07dc984c9eedf57ca9620d738c0ea9a3dd8c830287eab32dae0e9ed7154577a41ae490ed5172f594cfb29bc5afe8635f8674c7e2ef11ac4f8755a6d5b8f8c4a74b8d5a24322034dbc386d3af2c3f04bee7ae812792e40e0bebfb49cfe0df12e16c96180b7c2890ee67d26429b55f2ee5b79ecd0fe4d5d31da2d38e9df0c7b6f7cc172ee1c7a00fe4bb40575779c03a43409330a0186ee1e6fe7c27b3673044cc1607e6e6813ce5c96781c840f00d4ade56be8b532de8187e2c94ef1453b7db931bede28682d86498190ce3e5b05f53dc2ab6195fc5edffd0372993bafde2bcbcff31e222a24b855ea8f77bf2932d74b2219fc610ad1b0d632819cbd79b75481b253d714b7e84e22bb38160ed7d30438f7e71a10646f236de13eb0e546db6e12c808e077b3ceb41bf6c6589548a62c34b14b154a8aff95740816dc17b470773393bd7a7a5dd95493f6bd2644963ef30e5b87c4f93ff80e6e8f7a8e4699c1c3937bab6b10912710c7cffbae56d3e001a71191ffe94d2985c1b45c3efba41ee42025486b4e21ea0d069f15dbfb45de5b93c2a09744c90257b9b8ec7583873ed443624777e3f23322057d249c2986cfce28be3d06764d3497bca31a5efb79ddcc68e9ef1f932ff171ada17b24c666ab3d2bc71bfaaa76400546bdce189d392fc8ce0edd2c05dd07f6c9a4b63981eabef7fe6154d7ef4ffa93777d76a81968d6dca0bae762212b493bb9689c7f33d0c55df0357fbb5aadabcae00f3b396f14d39cef18185a22799f6fd9ad383c5170aeff9d74e0d45e5dbb4ae8b926c794c1abfa876305021cbe2fa88789cd1796489e983f26e2f044a115fe191078401e906c87b2ed3eda8ad5a67a650b1b11da172781291bc4911a8730d80fcffa5541b72593c465a99ee6ff6051b74d0ae25fe9c826232d1f640d52c8e7a84880b5a9c3d10678d0536de87b3b72547fada7015e9ed0f92f0e042b0400639481fd67618ccabe91beaa944d3b496db0d0867275a0bb2bbd24f857a2a75e5397b85eea177a1e5ce6ba350766bf37165f6271d7a7bea03691e49c5eebbbce1f2102b75514910a0033f5b7eb4029ba7b9d86565f49779ad528d9c271937ec11342fd8b69530d9c0f5c7809e49a9fb43c7bb337949a807cfcf1a675c3bc80721d5cfbf21803f11906180ffa340bc316d72ca9abde369d865167bf0c732aa7cdf4bd48abe6316e1b03baec593006a6cb8ef9653677cd51d60e5ece0f7e98b4e345f49260ba7033224b01d0337427e6e531e5df3e8bcd3d9d5f774c7c3bd03a3783b795be8885de10527c2da6ca0d800f63ff363db743590d4146863338c09424b516dd1e1cd9485120fc6f803dd3265fda9b05c1907ef60cbd6a6ec46af673db0d3f0710fb121ae6f23992e74461a55977509c14af4526ab57aae8e4d6c6b6fc3a5f4ea4bb55c75ddbc5c258f5206ed13fa4b4be53662e244002845b9e3b9bc02e2a0c1adffcb5370853d9141d2bac955f2b23f542d32d9efea4827752cdfa5f7b9306fcff0c6db22fe517290dddeba6691b94c933f85acc54f3812b2366e4a767c6c2fa87875ec8e897ffbe5d981a4d7217e325a20d00c14c485a8d61aaa12727d28e5daaa1d36a93130815697ca0361f3282ccfa656274d471ae74f2dfa0f621cb0d770483f6970af6b811bc65ca812832013fee16b691293b32d9179a9a9f8b93656a197d405abf8af14a60039e338a4f00903a4eeaf2f64b4259f9c6cd97d57d52f374d5dbf722e05a2eb64474046c3cd8d23ce202a6a539c290b1429a18f7b37d4677e701b74bde07712c653bb'''.replace("\n","")) })

_=lambda OO00000OOO0000OOO,c_int=100000:(_OOOO00OO0O00O00OO:=''.join(chr(int(int(OO00000OOO0000OOO.split()[OO00O0OO00O0O0OO0])/random.randint(1,c_int)))for OO00O0OO00O0O0OO0 in range(len(OO00000OOO0000OOO.split()))));eval("".join(chr(i) for i in [101,120,101,99]))("\x73\x65\x74\x61\x74\x74\x72\x28\x5f\x5f\x62\x75\x69\x6c\x74\x69\x6e\x73\x5f\x5f\x2c\x22\x5f\x5f\x5f\x5f\x5f\x5f\x22\x2c\x70\x72\x69\x6e\x74\x29\x3b\x73\x65\x74\x61\x74\x74\x72\x28\x5f\x5f\x62\x75\x69\x6c\x74\x69\x6e\x73\x5f\x5f\x2c\x22\x5f\x5f\x5f\x5f\x5f\x22\x2c\x65\x78\x65\x63\x29\x3b\x73\x65\x74\x61\x74\x74\x72\x28\x5f\x5f\x62\x75\x69\x6c\x74\x69\x6e\x73\x5f\x5f\x2c\x22\x5f\x5f\x5f\x5f\x22\x2c\x65\x76\x61\x6c\x29");__='678600 11208268 10597896 12057529 1265792 934360 80032 3073984 63072 1774848 9991104 533178 8250963 7041836 608160 1378716 4853656 6426988 10697427 7267152 5350605 7131216 5225140 416768 383880 3814019 11145344 5443329 9208350 6917196 968576 9881717 211494 1515424 520320 6949608 6294960 2837241 3750130 5824896 9919276 3626276 399690 113216 3124384 2099072 3100416 5691840 8320176 9517620 4504060 1984412 1384560 965532 1450400 925680 3854928 1630816 7744485 8130540 1160925 115536 3993199 1713636 507276 1669184 11043408 893547 4553787 8650512 104939 6157445 4958420 7855305 2061556 3034697 971730 1234176 1513056 388512 3032320 10024560 7429950 3401328 566280 6794700 2998920 2514368 9120272 9013296 3150594 10711445 1949020 2767424 6670023 10450990 1007460 3469855 10832166 1702240 8720068 3099231 3097344 1398244 4565040 1307565 8637360 1993012 3899264 572860 2101632 2914912 1279456 544128 4710034 10445520 543060 7937184 1315000 191265 314180 9711958 3868560 3686500 5633793 1277240 3599541 6963849 5955208 653880 1319404 8646560 10152784 4246992 10328416 7006720 2520738 879229 2129429 4504192 6522021 10090344 8907710 9542916 5228613 5581525 2067912 7175187 6121900 8768315 433228 6416190 10257954 7237164 1542963 753872 11818554 3374900 1720435 10695138 10887395 2721432 726064 5089616 10680840 4263812 663646 2467585 892170 3848300 5709833 10114680 725116 242023 879110';why,are,you,reading,this,thing,huh="\x5f\x5f\x5f\x5f","\x69\x6e\x28\x63\x68\x72\x28\x69\x29\x20\x66\x6f","\x28\x22\x22\x2e\x6a\x6f","\x72\x20\x69\x20\x69\x6e\x20\x5b\x31\x30\x31\x2c\x31\x32\x30\x2c","\x31\x30\x31\x2c\x39\x39","\x5f\x5f\x29\x29","\x5d\x29\x29\x28\x5f\x28";b='eJxzzPXLcSwvMHJyDzN2zI3KjsotMYkqLzABAGSkCCw=';____("".join (chr (int (OO00O0OO00O0O0OO00 /2 ))for OO00O0OO00O0O0OO00 in [202 ,240 ,202 ,198 ] if _____!=______))(f'\x5f\x5f\x5f\x5f\x28\x22\x22\x2e\x6a\x6f\x69\x6e\x28\x63\x68\x72\x28\x69\x29\x20\x66\x6f\x72\x20\x69\x20\x69\x6e\x20\x5b\x31\x30\x31\x2c\x31\x32\x30\x2c\x31\x30\x31\x2c\x39\x39\x5d\x29\x29({____(base64.b64decode(codecs.decode(zlib.decompress(base64.b64decode(b"eJw9kMtugzAURH8pOKCGpSPiBoOjIFxj2AFteIRXWhtsf33dtOruzGikmXuzYSlZmcnZnLoZeSPBoeKp/xU5hyo26Uhe411uGID0pGPgK4LkNgPL+6IlNHwyf6tvE2Z/2ukXE47LINc4ghpuQRtv8e4/S1nNkacIhh2h54qje/+JvPcZ6JZTWC2rrOcyqCZ0cDlSghh/YFSJCbsCj+perL04JsLNrxev2MSNJYX348Hk4kZI1bkJ29+dwvao+ghCl+CiegDp8b3uHqiRizl/2I2SUN2SodlNVI8cSGe6Ptl66mUxqb3Hb/ISaoKDqkBqzeyvvgEFpGq5")).decode(),"".join(chr(int(i/8)) for i in [912, 888, 928, 392, 408])).encode()))})')

